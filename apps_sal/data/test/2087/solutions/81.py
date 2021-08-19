import itertools
(a, b, c) = list(map(int, input().split()))
ans = a * b * c * (a + 1) * (b + 1) * (c + 1) // 8
print(ans % 998244353)
