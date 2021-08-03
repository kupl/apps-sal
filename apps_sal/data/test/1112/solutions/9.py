a = [list(map(int, input().split())) for i in range(3)]
a[0][0] = int((sum(a[1]) + sum(a[2]) - sum(a[0])) / 2)
sum_1 = sum(a[0])
a[1][1] = sum_1 - sum(a[1])
a[2][2] = sum_1 - sum(a[2])
for i in range(3):
    print(a[i][0], a[i][1], a[i][2])
