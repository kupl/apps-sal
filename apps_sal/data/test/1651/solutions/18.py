import math


def factor(n):
    l = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            l.append(i)
    if n > 2:
        l.append(n)
    return l


s, p = map(int, input().split())
l = factor(p)
# print(l)
n = len(l)
for i in range(n):
    x = (p // l[i]) + l[i]
    if x == s:
        flag = True
        break
    else:
        flag = False
if flag:
    print("Yes")
else:
    print("No")
