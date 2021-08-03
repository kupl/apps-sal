from collections import defaultdict

n = int(input())
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

q = defaultdict(int)
w = defaultdict(int)
e = defaultdict(int)

for a in aa:
    q[a] += 1
    e[a] += 1

for b in bb:
    w[b] += 1
    e[b] += 1

ans = 0
for i in range(1, 6):
    if e[i] % 2 != 0:
        ans = -1
        break
    ans += abs(q[i] - (e[i] // 2))

print(ans // 2)
