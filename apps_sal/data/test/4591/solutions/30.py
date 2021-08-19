(A, B, C, X, Y) = map(int, input().split())
moneys = []
for i in range(0, 2 * max(X, Y) + 1, 2):
    if X - i // 2 >= 0 and Y - i // 2 >= 0:
        moneys.append((X - i // 2) * A + (Y - i // 2) * B + C * i)
    elif X - i // 2 >= 0 and Y - i // 2 < 0:
        moneys.append((X - i // 2) * A + C * i)
    elif X - i // 2 < 0 and Y - i // 2 >= 0:
        moneys.append((Y - i // 2) * B + C * i)
    else:
        moneys.append(C * i)
print(min(moneys))
