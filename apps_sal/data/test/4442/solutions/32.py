a, b = map(str, input().split())
A = a * int(b)
B = b * int(a)
print(sorted([A, B])[0])
