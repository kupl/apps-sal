n, k = list(map(int, input().split()))


a = n % k
b = k - a
print((min(a, b)))
