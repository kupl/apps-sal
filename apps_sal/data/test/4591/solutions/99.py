(A, B, C, X, Y) = map(int, input().split())
p_A = A * X
p_B = B * Y
total = p_A + p_B
if X > Y:
    a = X - Y
    ab = Y * C * 2
    total_ab = C * X * 2
    total_1 = ab + a * A
    print(min(total_1, total, total_ab))
elif X < Y:
    b = Y - X
    ab = X * C * 2
    total_ab = C * Y * 2
    total_2 = ab + b * B
    print(min(total_2, total, total_ab))
elif X == Y:
    ab = C * X * 2
    print(min(ab, total))
