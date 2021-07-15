def mountain(a, b):
    z = list()
    for i in range(1, a + 1):
        z.append(i)
    for i in range(a + b + 1, a, -1):
        z.append(i)
    return z


A = int(input())
B = int(input())
print(*mountain(A, B))

