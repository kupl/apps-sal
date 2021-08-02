a = [list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))]
N = int(input())
b = list()
for i in range(0, N):
    b.append(int(input()))
for j in range(0, 3):
    for k in range(0, 3):
        for i in range(0, N):
            if a[j][k] == b[i]:
                a[j][k] = 0
for i in range(0, 3):
    if a[i][0] == a[i][1] and a[i][1] == a[i][2]:
        print("Yes")
        break
    elif a[0][i] == a[1][i] and a[1][i] == a[2][i]:
        print("Yes")
        break
    elif a[0][0] == a[1][1] and a[1][1] == a[2][2]:
        print("Yes")
        break
    elif a[2][0] == a[1][1] and a[1][1] == a[0][2]:
        print("Yes")
        break
else:
    print("No")
