n = int(input())
a = [[0, 0, 0]]

for i in range(n):
    a.append(list(map(int, input().split(" "))))
for i in range(n):
    check = a[i + 1][0] - a[i][0] - (abs(a[i + 1][1] - a[i][1]) + abs(a[i + 1][2] - a[i][2]))
    if check >= 0 and check % 2 == 0:
        continue
    else:
        print("No")
        break
else:
    print("Yes")
