N = int(input())
c = list(map(int, input().split()))
c.sort()
m = 10**9 + 7
ans = 0
for i in range(N):
    ans += (c[i] * (N - i + 1) * pow(2, (N - 2) % (m - 1), m)) % m
print((ans * pow(2, N, m)) % m)
