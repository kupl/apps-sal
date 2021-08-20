(k, a, b) = map(int, input().split())
if a % k:
    a += k - a % k
b -= b % k
print(b // k - a // k + 1)
