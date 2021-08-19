from sys import stdin, stdout
n = int(stdin.readline().strip())
s = list(map(int, stdin.readline().strip().split()))
vis = [False for i in range(n + 10)]
for i in s:
    vis[i] = True
nu = []
nu1 = []
for i in range(1, n + 1):
    if not vis[i]:
        if s[i - 1] == 0:
            nu.append(i)
        else:
            nu1.append(i)
nu.sort()
while len(nu) >= 2:
    if len(nu) % 2 != 0:
        s[nu[-3] - 1] = nu[-1]
        s[nu[-1] - 1] = nu[-2]
        s[nu[-2] - 1] = nu[-3]
        nu.pop()
        nu.pop()
        nu.pop()
        continue
    s[nu[-1] - 1] = nu[-2]
    s[nu[-2] - 1] = nu[-1]
    nu.pop()
    nu.pop()
if len(nu) == 1:
    s[nu[-1] - 1] = nu1[-1]
    nu1.pop()
    nu1.append(nu[-1])
for i in range(n):
    if s[i] == 0:
        s[i] = nu1[-1]
        nu1.pop()
print(*s)
