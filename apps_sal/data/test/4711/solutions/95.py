a, b, c = map(int, input().split())

sums = [a + b, b + c, c + a]

print(min(sums))
