N, K = list(map(int, input().split()))
MOD = 10 ** 9 + 7
lst = [0] + [pow(K // d, N, MOD) for d in range(1, K + 1)]

for d in range(K, 0, -1):
    lst[d] -= sum(lst[d * i] for i in range(2, K // d + 1))

ans = 0
for i, x in enumerate(lst):
    ans = (ans + i * x) % MOD
print(ans)

