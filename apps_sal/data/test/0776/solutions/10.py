a, b, c = list(map(int, input().split()))
n, u0, u1 = int(input()), [], []
for i in range(n):
    e0, e1 = input().split()
    if e1 == 'USB':
        u0.append(int(e0))
    else:
        u1.append(int(e0))
u0.sort()
u1.sort()
n = 0
x = 0
if len(u0) > a:
    x = x + sum(u0[:a])
    u0 = u0[a:]
    n = n + a
else:
    x = x + sum(u0)
    n = n + len(u0)
    u0 = []
if len(u1) > b:
    x = x + sum(u1[:b])
    u1 = u1[b:]
    n = n + b
else:
    x = x + sum(u1)
    n = n + len(u1)
    u1 = []
u = u1 + u0
u.sort()
if len(u) > c:
    x = x + sum(u[:c])
    n = n + c
else:
    x = x + sum(u)
    n = n + len(u)
print(str(n) + ' ' + str(x))
