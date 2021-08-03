X, Y = map(int, input().split())
if 2 * Y < X or 2 * X < Y:
    print(0)
    return
if not((X % 3 == 0 and Y % 3 == 0) or (X % 3 == 1 and Y % 3 == 2) or (X % 3 == 2 and Y % 3 == 1)):
    print(0)
    return
P = 10**9 + 7
A = (2 * Y - X) // 3
B = (2 * X - Y) // 3
num = 1
for i in range(A + 1, A + B + 1):
    num = num * i % P
den = 1
for j in range(1, B + 1):
    den = den * j % P
den = pow(den, P - 2, P)
print((num * den) % P)
