n = int(input())
x_b, y_b = list(map(int, input().split()))
dif_b = 0
cnt = 0

for i in range(n - 1):
    x, y = list(map(int, input().split()))
    if x > x_b:
        dif = 1
    elif x < x_b:
        dif = 3
    elif y > y_b:
        dif = 0
    elif y < y_b:
        dif = 2

    if (dif_b == 1 and dif == 0) or (dif_b == 0 and dif == 3) or (dif_b == 3 and dif == 2) or (dif_b == 2 and dif == 1):
        cnt += 1

    x_b = x
    y_b = y
    dif_b = dif

print(cnt)
