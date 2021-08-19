n = int(input())
(u, v) = ([0] * n, [0] * 100001)
for i in range(n):
    (x, y) = map(int, input().split())
    u[i] = y
    v[x] += 1
for i in range(n):
    k = v[u[i]]
    u[i] = str(n - 1 + k) + ' ' + str(n - 1 - k)
print('\n'.join(u))
