(k, a, b) = map(int, input().split())
a = ((a - 1) // k + 1) * k
b -= b % k
print(max(0, (b - a + 1) // k + (k != 1)))
