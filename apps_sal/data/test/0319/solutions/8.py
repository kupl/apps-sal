(n, m) = list(map(int, input().split()))

lst = []
for x in range(n):
    lst.append(input())

array = [0] * m
for x in range(n):
    for y in range(m):
        if lst[x][y] == '1':
            array[y] += 1

F = False
for x in range(n):
    flag = True
    for y in range(m):
        if lst[x][y] == '1' and array[y] == 1:
            flag = False
    if flag:
        F = True
        break

if F:
    print("YES")
else:
    print("NO")

