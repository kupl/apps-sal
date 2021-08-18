N, M = map(int, input().split())
l, r = [0] * N, [0] * N
for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        l[b - 1] = 1
    if b == N:
        r[a - 1] = 1
for i in range(N):
    if l[i] + r[i] == 2:
        print('POSSIBLE')
        return
print('IMPOSSIBLE')
