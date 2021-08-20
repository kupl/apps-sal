(n, p) = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(input())
apples = 0
welth = 0
for i in range(n - 1, -1, -1):
    if l[i] == 'halfplus':
        apples = apples * 2 + 1
    else:
        apples = apples * 2
    welth += apples * p // 2
print(welth)
