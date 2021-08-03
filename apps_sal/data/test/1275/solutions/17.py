from math import comb

N, K = list(map(int, input().split()))

ans = comb(K + 2 * N + 1, 3)
for i in range(1, 5):
    if K + 2 * N + 1 - i * N >= 0:
        ans += (-1)**i * comb(K + 2 * N + 1 - i * N, 3) * comb(4, i)

print(ans)
