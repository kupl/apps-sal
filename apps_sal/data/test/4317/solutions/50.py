a, b = map(int, input().split())

sum = a + b
sub = a - b
mul = a * b

print(max(sum, sub, mul))
