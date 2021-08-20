(n, k) = list(map(int, input().split()))
m = 1000000007
print(pow(k, k - 1, m) * pow(n - k, n - k, m) % m)
