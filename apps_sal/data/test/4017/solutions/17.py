import math
n = int(input())


def fun(itm):
    return itm[0]


def sm(l):
    s = 0
    for i in l:
        s += i[0]
    return s


l1 = list(map(int, input().split()))
for i in range(n):
    l1[i] = [l1[i], i]
ans = []
l = sorted(l1, key=fun)
s = sm(l) - l[n - 1][0]
for i in range(n - 1):
    if(s - l[i][0] == l[n - 1][0]):
        ans.append(l[i][1] + 1)
if(s - l[n - 2][0] == l[n - 2][0]):
    ans.append(l[n - 1][1] + 1)
print(len(ans))
for i in ans:
    print(i, end=" ")
