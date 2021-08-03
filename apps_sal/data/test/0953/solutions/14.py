
n = int(input())
p = [int(i) for i in input().split()]
s = ()
for i in range(n):
    s += (input(),)
z = [False] * n
x, y = [], []


def dfs(i):
    if not z[i]:
        nonlocal x
        z[i] = True
        x.append(i)
        y.append(p[i])
        for j in range(n):
            if s[i][j] == '1':
                dfs(j)


for i in range(n):
    if not z[i]:
        x, y = [], []
        dfs(i)
        x.sort()
        y.sort()
        for j in range(len(x)):
            p[x[j]] = y[j]

print(" ".join([str(i) for i in p]))
