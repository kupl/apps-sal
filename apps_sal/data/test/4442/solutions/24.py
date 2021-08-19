(a, b) = map(str, input().split())
A = a * int(b)
B = b * int(a)
x = [A, B]
x.sort()
print(x[0])
