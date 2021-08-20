n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
sum = 0
for i in range(n):
    for j in range(i + 1, n):
        sum += ((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2) ** 0.5
print(2 * sum / n)
