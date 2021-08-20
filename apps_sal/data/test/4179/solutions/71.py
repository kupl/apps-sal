(n, m, c) = (int(i) for i in input().split())
list_b = [int(i) for i in input().split()]
list_a = [[int(i) for i in input().split()] for j in range(0, n)]
count = 0
tmp = 0
for i in range(0, n):
    for j in range(0, m):
        tmp += list_b[j] * list_a[i][j]
    tmp += c
    if tmp > 0:
        count += 1
    tmp = 0
print(count)
