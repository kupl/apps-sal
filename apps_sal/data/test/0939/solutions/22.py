def intinp():
    return list(map(int, input().split()))


n, m = intinp()
Color = [0 for i in range(n + 1)]
for i in range(m):
    u = [0]
    u = u + intinp()
    if Color[u[1]]:
        u[Color[u[1]]], u[1] = u[1], u[Color[u[1]]]
    if Color[u[2]]:
        u[Color[u[2]]], u[2] = u[2], u[Color[u[2]]]
    if Color[u[3]]:
        u[Color[u[3]]], u[3] = u[3], u[Color[u[3]]]
    Color[u[1]] = 1
    Color[u[2]] = 2
    Color[u[3]] = 3
print(" ".join(list(map(str, Color[1:]))))
