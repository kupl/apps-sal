import itertools
n = int(input())
s = [[] for i in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        (x, y) = [int(x) for x in input().split()]
        x -= 1
        s[i].append([x, y])
l = []
a = itertools.product(range(2), repeat=n)
for i in a:
    l.append(i)
ans = 0
for i in range(2 ** n):
    c = []
    for j in range(n):
        if l[i][j] == 1:
            for k in s[j]:
                if l[i][k[0]] != k[1]:
                    c.append(False)
    if c == []:
        ans = max(ans, sum(l[i]))
print(ans)
