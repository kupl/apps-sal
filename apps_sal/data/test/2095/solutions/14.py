a = int(input())
x = []
for i in range(a):
    x.append([int(x) for x in input().split()])
ans = []
for i in range(a):
    cont = True
    for j in range(a):
        if x[i][j] == 1 or x[i][j] == 3:
            cont = False
    if cont:
        ans.append(i + 1)
print(len(ans))
print(*ans)
