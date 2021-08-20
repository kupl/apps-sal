import math
(A, B, C, X, Y) = map(int, input().split())
saishou = math.inf
temp = 0
for i in range(0, X + 1):
    temp = A * i + C * 2 * (X - i)
    if X - i < Y:
        if 2 * C <= B:
            temp += 2 * C * (Y - (X - i))
        else:
            temp += B * (Y - (X - i))
    if saishou > temp:
        saishou = temp
print(saishou)
