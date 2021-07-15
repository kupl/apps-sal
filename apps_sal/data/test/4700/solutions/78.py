import copy

n,m = list(map(int, input().split()))
h = [0] + list(map(int, input().split()))

towers = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = list(map(int, input().split()))
    towers[a].append(b)
    towers[b].append(a)

cnt = 0
for i in range(1, n + 1):
    for j in towers[i]:
        if h[i] <= h[j]:
            break
    else:
        cnt += 1

print(cnt)
            

