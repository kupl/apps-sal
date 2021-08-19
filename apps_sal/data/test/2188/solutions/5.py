n = int(input())
v = []
u = []
for i in range(n):
    x = input().split(' ')
    a = int(x[0])
    b = int(x[1])
    if a > b:
        v.append((a, b, i + 1))
    else:
        u.append((a, b, i + 1))
'nr = 1\nsol = [str(v[0][2])]\nact = v[0][1]\ni = 1\nn = len(v)\nwhile i < n:\n\twhile i < n and v[i][0] < act:\n\t\ti += 1\n\tif i < n:\n\t\tnr += 1\n\t\tsol.append(str(v[i][2]))\n\t\tact = v[i][1]\n\t\ti += 1\n\nu = sorted(uv, key = lambda x:x[1])\nnr2 = 1\nsol2 = [str(u[0][2])]\nact = u[0][1]\ni = 1\nn = len(u)\nwhile i < n:\n\twhile i < n and u[i][0] < act:\n\t\ti += 1\n\tif i < n:\n\t\tnr2 += 1\n\t\tsol2.append(str(u[i][2]))\n\t\tact = u[i][1]\n\t\ti += 1'
if len(u) > len(v):
    u = sorted(u, key=lambda x: x[1], reverse=True)
    print(len(u))
    sol = []
    for i in range(len(u)):
        sol.append(str(u[i][2]))
    print(' '.join(sol))
else:
    v = sorted(v, key=lambda x: x[1], reverse=False)
    print(len(v))
    sol = []
    for i in range(len(v)):
        sol.append(str(v[i][2]))
    print(' '.join(sol))
