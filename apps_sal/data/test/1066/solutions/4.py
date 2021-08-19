(a, b) = list(map(int, input().split()))
c = b - (a + 1) // 2
print(2 * c if c > 0 else 2 * b - 1)
