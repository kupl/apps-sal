n = int(input())
counter = 0
a = [[0 for j in range(n)] for i in range(n)]
for i in range(n - 1):
    (i, j) = map(int, input().split())
    a[i - 1][j - 1] = 1
    a[j - 1][i - 1] = 1
for element in a:
    if element.count(1) == 1:
        counter += 1
print(counter)
