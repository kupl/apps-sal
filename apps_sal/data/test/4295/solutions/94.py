n, k = map(int, input().split())

print((n % k) if (n % k) < (k - (n % k)) else (k - (n % k)))
