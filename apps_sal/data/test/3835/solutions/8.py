n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
a1 = round((a[0][1] * a[0][2] // a[1][2]) ** 0.5)
print(a1, end=" ")
for i in range(1, n):
    print(a[i][0] // a1, end=" ")
