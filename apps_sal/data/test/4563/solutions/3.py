n = int(input())
A, B = 0, 0
for i in range(n):
    x, y = map(int, input().split())
    dx, dy = 1, 1
    if A > x:
        dx = A // x
        if A % x != 0:
            dx += 1

    if B > y:
        dy = B // y
        if B % y != 0:
            dy += 1

    a = max(dx, dy)
    A, B = a * x, a * y
print(A + B)
