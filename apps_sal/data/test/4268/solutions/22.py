import math
n, d = list(map(int,input().split()))
lst = []
for i in range(n):
    x = list(map(int,input().split()))
    lst.append(x)
def check (lst, a, b):
    tmp = 0
    for i in range(len(lst[a])):
        tmp = tmp + (lst[a][i] - lst[b][i])**2
    tmp = math.sqrt(tmp)
    if (tmp//1 == tmp):
        return (1)
    else:
        return (0)
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans = ans + check(lst, i, j)
print(ans)

