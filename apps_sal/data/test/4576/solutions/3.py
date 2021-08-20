A = int(input())
B = int(input())
C = int(input())
X = int(input())
cnt = 0
rest_X = 0
for i in range(0, A + 1):
    rest_X = X - 500 * i
    if rest_X == 0:
        cnt += 1
        break
    elif rest_X < 0:
        break
    for j in range(0, B + 1):
        rest_X = X - 500 * i
        rest_X = rest_X - 100 * j
        if rest_X == 0:
            cnt += 1
            break
        elif rest_X < 0:
            break
        if 50 * C >= rest_X:
            cnt += 1
print(cnt)
