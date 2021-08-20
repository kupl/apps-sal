import math
(n, k) = map(int, input().split())
for i in range(1, k + 1):
    ans = math.comb(n - k + 1, i) * math.comb(k - 1, i - 1)
    print(ans % (10 ** 9 + 7))
