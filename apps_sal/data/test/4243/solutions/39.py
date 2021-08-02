X = int(input())
answer = 0


a = X // 500
b = X - 500 * a
c = b // 5

if a >= 0 and c >= 0:
    print((a * 1000 + c * 5))
elif X % 500 == 0:
    print((a * 1000))
elif X < 500:
    print((c * 5))
elif X == 0:
    print((0))
