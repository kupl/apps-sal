n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

N = int(1e5+4)
is_prime = [0] * N
is_prime[0] = is_prime[1] = 1
for i in range(2, N):
    if is_prime[i] == 1: continue
    for j in range(i*2, N, i):
        is_prime[j] = 1
is_prime[-1] = N - 1
for i in range(N-2, 0, -1):
    if is_prime[i] == 1:
        is_prime[i] = is_prime[i + 1]
    else:
        is_prime[i] = i
r, c = [0] * n, [0] * m
for i in range(n):
    for j in range(m):
        r[i] += is_prime[arr[i][j]] - arr[i][j]
        c[j] += is_prime[arr[i][j]] - arr[i][j]
print(min(r + c))

