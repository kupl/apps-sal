a, b = list(map(int, input().split()))

A = []
for x in range(1, 7):
    if (abs(a - x) < abs(b - x)):
        A.append(x)
    else:
        continue

B = []
for y in range(1, 7):
    if (abs(b - y) < abs(a - y)):
        B.append(y)
    else:
        continue

D = []
for i in range(1, 7):
    if (abs(a - i) == abs(b - i)):
        D.append(i)
    else:
        continue


print(str(len(A)) + " " + str(len(D)) + " " + str(len(B)))
