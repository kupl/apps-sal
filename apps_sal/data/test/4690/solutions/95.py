
A, B, C, D = map(int, input().split())

x = A * B
y = C * D
if x > y:
    print(x)
elif x < y:
    print(y)
elif x == y:
    print(x)
