N, M = map(int, input().split())
H = list(map(int, input().split()))
H.insert(0, 0)
t = [True] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    if H[a] <= H[b]:
        t[a] = False
    if H[b] <= H[a]:
        t[b] = False

c = 0
for i in range(1, N+1, 1):
    if t[i]:
        c += 1

print(c)
