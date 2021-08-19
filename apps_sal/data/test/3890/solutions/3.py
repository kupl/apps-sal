(n, k) = map(int, input().split())
d = 1000000007
print(pow(k, k - 1, d) * pow(n - k, n - k, d) % d)
