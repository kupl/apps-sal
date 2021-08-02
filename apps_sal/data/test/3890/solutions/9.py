n, k = map(int, input().split())
n -= k
print(k**(k - 1) * n**n % 1000000007)
