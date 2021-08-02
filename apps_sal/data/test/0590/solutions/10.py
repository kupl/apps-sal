from collections import defaultdict

n = int(input())
l = list(map(int, input().split()))

count = defaultdict(int)
for x in l:
    count[x] += 1

need = []

for x in range(1, n + 1):
    if count[x] == 0:
        need.append(x)

pos_need = 0
open = [False for _ in range(n + 1)]
actions = 0

for i in range(n):
    if pos_need == len(need):
        break
    if count[l[i]] >= 2:
        if l[i] < need[pos_need]:
            if open[l[i]]:
                count[l[i]] -= 1
                l[i] = need[pos_need]
                actions += 1
                pos_need += 1
            else:
                open[l[i]] = True
        else:
            count[l[i]] -= 1
            l[i] = need[pos_need]
            actions += 1
            pos_need += 1

print(actions)
print(*l)
