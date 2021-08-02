n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
a.insert(0, [0, 0, 0])
for i in range(n):
    b = a[i + 1][0] - a[i][0]
    c = abs(a[i + 1][1] + a[i + 1][2] - a[i][1] - a[i][2])
    if b < c or b % 2 != c % 2:
        print("No")
        break
else:
    print("Yes")
