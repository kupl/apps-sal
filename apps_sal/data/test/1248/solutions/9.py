a, b, c = list(map(int, input().split()))

print(min([a + b + c, a + a + b + b, a + c + c + a, b + c + c + b]))

