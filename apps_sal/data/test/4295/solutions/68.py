(n, k) = list(map(int, input().split()))
print(min(n % k, k - n % k))
