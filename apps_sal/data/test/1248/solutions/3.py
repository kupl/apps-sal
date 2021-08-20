(a, b, c) = map(int, input().split())
print(min(a + a + b + b, a + c + b, a + c + c + a, b + c + c + b))
