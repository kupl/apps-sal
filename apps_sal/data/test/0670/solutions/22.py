from math import sqrt


def ro(x, y):
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def make_y(k):
    return (-a * k - c) / b


def make_x(k):
    return (-b * k - c) / a


a, b, c = list(map(int, input().split()))
A = [0, 0]
B = [0, 0]
A[0], A[1], B[0], B[1] = list(map(int, input().split()))
if a == 0 or b == 0:
    print(abs(A[0] - B[0]) + abs(A[1] - B[1]))
else:
    ans = [abs(A[0] - B[0]) + abs(A[1] - B[1]),
           abs(make_y(A[0]) - A[1]) + abs(make_y(B[0]) - B[1]) + ro([A[0], make_y(A[0])], [B[0], make_y(B[0])]),
           abs(make_x(A[1]) - A[0]) + abs(make_y(B[0]) - B[1]) + ro([make_x(A[1]), A[1]], [B[0], make_y(B[0])]),
           abs(make_y(A[0]) - A[1]) + abs(make_x(B[1]) - B[0]) + ro([A[0], make_y(A[0])], [make_x(B[1]), B[1]]),
           abs(make_x(A[1]) - A[0]) + abs(make_x(B[1]) - B[0]) + ro([make_x(A[1]), A[1]], [make_x(B[1]), B[1]])]
    print(min(ans))

