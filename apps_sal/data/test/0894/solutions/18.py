I = [int(i) for i in input().split()]
x, y = I[0], I[1]
ans = int(abs(x) + abs(y))
A, C = [0, 0], [0, 0]
if x > 0 and y > 0:
    A[1], C[0] = ans, ans
if x > 0 and y < 0:
    A[1], C[0] = -ans, ans
if x < 0 and y > 0:
    A[0], C[1] = -ans, ans
if x < 0 and y < 0:
    A[0], C[1] = -ans, -ans
print(str(A[0]) + ' ' + str(A[1]) + ' ' + str(C[0]) + ' ' + str(C[1]))
