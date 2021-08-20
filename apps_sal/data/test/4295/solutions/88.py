(n, k) = map(int, input().split())
ans = n
print(min(n % k, k - n % k))
