g1 = [4, 6, 9, 11]
g2 = [2]

x, y = list(map(int, input().split()))
gx = 1 if x in g1 else 2 if x in g2 else 0
gy = 1 if y in g1 else 2 if y in g2 else 0
print(("Yes" if gx == gy else "No"))
