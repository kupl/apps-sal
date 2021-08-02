n = int(input())

b1 = [[int(x) for x in input()] for _ in range(n)]
input()
b2 = [[int(x) for x in input()] for _ in range(n)]
input()
b3 = [[int(x) for x in input()] for _ in range(n)]
input()
b4 = [[int(x) for x in input()] for _ in range(n)]


def cost(b):
    z = o = 0
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == b[i][j]:
                z += 1
            if (i + j + 1) % 2 == b[i][j]:
                o += 1
    return z, o


z1, o1 = cost(b1)
z2, o2 = cost(b2)
z3, o3 = cost(b3)
z4, o4 = cost(b4)

print((min(
    z1 + z2 + o3 + o4,
    z1 + o2 + z3 + o4,
    z1 + o2 + o3 + z4,
    o1 + z2 + z3 + o4,
    o1 + z2 + o3 + z4,
    o1 + o2 + z3 + z4,
)))
