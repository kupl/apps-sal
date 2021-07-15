a, b, c = list(map(int, input().split(' ')))

print((((b - 1 + c) % a) + a) % a + 1)

