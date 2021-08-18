N = int(input())

a = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    if i == 0:
        if (a[i][0] - a[i][1] - a[i][2]) % 2 != 0 or (a[i][0] - a[i][1] - a[i][2]) < 0:
            print("No")
            return
    else:
        if (a[i][0] - a[i][1] - a[i][2]) % 2 != 0 or (a[i][0] - a[i - 1][0]) - ((a[i - 1][1] + a[i - 1][2]) - (a[i][1] + a[i][2])) < 0:
            print("No")
            return
print("Yes")
