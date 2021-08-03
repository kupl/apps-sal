n = int(input())
A, B = 0, 0
for i in range(n):
    x, y = map(int, input().split())
    t, a = 1, 1
    if A > x:
        t = A // x
        if A % x != 0:
            t += 1
    if B > y:
        a = B // y
        if B % y != 0:
            a += 1
    m = max(t, a)
    A = x * m
    B = y * m
print(A + B)
