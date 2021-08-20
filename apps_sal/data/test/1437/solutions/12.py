A = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
Z = [0] * 64
for i in range(64):
    r = 0
    for j in range(64):
        for k in range(64):
            if i == j & k:
                r += 1
    Z[i] = r
r = 1
for c in input():
    r = r * Z[A.index(c)] % 1000000007
print(r)
'\nV_V & V_V = V_V\n\n__V & V_V = V_V\nV_V & __V = V_V\n\nV__ & V_V = V_V\nV_V & V__ = V_V\n\n___ & V_V = V_V\nV_V & ___ = V_V\n\n__V & V__ = V_V\nV__ & __V = V_V\n'
