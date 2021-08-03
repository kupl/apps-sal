a, b, c, d = list(map(int, input().split()))
calc = [a * c, a * d, b * c, b * d]
print(max(calc))
