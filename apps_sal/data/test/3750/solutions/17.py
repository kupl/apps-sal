k, a, b = list(map(int, input().split()))
count = a // k + b // k
print(-1 if (not count) or (a < k and b % k) or (b < k and a % k) else count)

