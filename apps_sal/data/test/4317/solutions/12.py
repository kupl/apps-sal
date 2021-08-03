a, b = map(int, input().split())

compare = max(a + b, a - b, a * b)
print(compare)
