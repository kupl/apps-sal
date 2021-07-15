import sys, math

n, m = list(map(int, input().split()))

a = ["" for i in range(n)]
for i in range(n):
    a[i] = input()

if (a[0][0] == a[0][m-1]) and (n % 3 == 0):
    for i in range(n // 3):
        for j in range(m):
            if (not a[i][j] == a[0][0]):
                print("NO")
                return
    for i in range(n // 3, 2 * n // 3):
        for j in range(m):
            if (not a[i][j] == a[n // 3][0]):
                print("NO")
                return
    for i in range(2 * n // 3, n):
        for j in range(m):
            if (not a[i][j] == a[2 * n // 3][0]):
                print("NO")
                return
    if (a[0][0] == a[n // 3][0]) or (a[0][0] == a[2 * n // 3][0]) or (a[2 * n // 3][0] == a[n // 3][0]):
        print("NO")
        return
    else:
        print("YES")
        return
elif (a[0][0] == a[n - 1][0]) and (m % 3 == 0):
    for i in range(n):
        for j in range(m // 3):
            if not ((a[i][j] == a[0][0]) and (a[i][j + m // 3] == a[0][m // 3]) and (
                a[i][j + 2 * m // 3] == a[0][2 * m // 3])):
                print("NO")
                return
    if (a[0][0] == a[0][m // 3]) or (a[0][0] == a[0][2 * m // 3]) or (a[0][2 * m // 3] == a[0][m // 3]):
        print("NO")
        return
    else:
        print("YES")
else:
    print("NO")

