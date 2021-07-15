a, b = map(int, input().split())

a1 = a * str(b)
a2 = b * str(a)
print(min(a1, a2))
