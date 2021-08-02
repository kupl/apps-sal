a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]

for i in b:
    for j in range(0, 3):
        for k in range(0, 3):
            if i == a[j][k]:
                a[j][k] = 0


if a[0][0] == 0 and a[0][1] == 0 and a[0][2] == 0:
    print("Yes")
elif a[1][0] == 0 and a[1][1] == 0 and a[1][2] == 0:
    print("Yes")
elif a[2][0] == 0 and a[2][1] == 0 and a[2][2] == 0:
    print("Yes")
elif a[0][0] == 0 and a[1][0] == 0 and a[2][0] == 0:
    print("Yes")
elif a[0][1] == 0 and a[1][1] == 0 and a[2][1] == 0:
    print("Yes")
elif a[0][2] == 0 and a[1][2] == 0 and a[2][2] == 0:
    print("Yes")
elif a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
    print("Yes")
elif a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
    print("Yes")
else:
    print("No")
