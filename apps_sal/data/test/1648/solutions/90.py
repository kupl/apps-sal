import math
n, k = map(int, input().split())
m = 10**9 + 7
for i in range(1, k + 1):
    print(math.comb(n - k + 1, i) * math.comb(k - 1, i - 1) % m)
