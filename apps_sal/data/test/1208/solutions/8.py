d = {}
z = 0
a = 0
n = int(input())
for e in range(n):
    u, v = input().split()
    v = int(v)
    if u == '+':
        z += 1
        d[v] = 1
    else:
        if d.get(v) == 1:
            d[v] = 0
            z -= 1
        else:
            a += 1
    a = max(a, z)
print(a)    

