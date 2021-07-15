n, m = list(map(int, input().split()))
h = list(map(int, input().split()))
neighbor = [[] for _ in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    neighbor[a - 1].append(b - 1)
    neighbor[b - 1].append(a - 1)

cnt = 0
for i in range(n):
    if all([h[i] > h[j] for j in neighbor[i]]):
        cnt += 1
print(cnt)
