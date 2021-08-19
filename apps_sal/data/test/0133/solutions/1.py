MOD = 1000000007
(n, m) = list(map(int, input().split()))
print(pow(pow(2, m, MOD) - 1, n, MOD))
