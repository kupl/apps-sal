(n, u) = (int(input()), list(map(int, input().split())))
v = list(sorted(u))
for i in range(n - 1):
    u[i + 1] += u[i]
    v[i + 1] += v[i]
(u, v) = ([0] + u, [0] + v)
for i in range(int(input())):
    (t, l, r) = map(int, input().split())
    print(u[r] - u[l - 1] if t == 1 else v[r] - v[l - 1])
