a, b, c, k = list(map(int, input().split()))

print((k if a > k else a - max(k - a - b, 0)))

