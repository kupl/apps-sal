a, b = map(int, input().split())

A = str(a) * b
B = str(b) * a

if a > b:
    print(B)
else:
    print(A)
