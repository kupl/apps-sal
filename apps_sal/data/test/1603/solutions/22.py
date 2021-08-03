n = int(input())
v = [int(x) for x in input().split()]
u = sorted(v)
m = int(input())
for i in range(1, n):
    v[i] += v[i - 1]
    u[i] += u[i - 1]
v.append(0)
u.append(0)
for i in range(m):
    t, l, r = [int(x) for x in input().split()]
    if t == 1:
        print(v[r - 1] - v[l - 2])
    else:
        print(u[r - 1] - u[l - 2])
