(N, M) = list(map(int, input().strip().split()))
inf = 10 ** 9 + 7
ans = 1
for n in range(1, N + 1):
    ans *= n
    ans %= inf
for m in range(1, M + 1):
    ans *= m
    ans %= inf
if abs(N - M) >= 2:
    print(0)
elif abs(N - M) == 1:
    print(ans)
else:
    print(ans * 2 % inf)
