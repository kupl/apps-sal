(a, b) = list(map(int, input().split()))
print(a + b - a * 2 * (b % a != 0))
