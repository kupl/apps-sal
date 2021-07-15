p = [tuple(map(int, input().split())) for i in range(3)]
if p[0][0] == p[1][0] and p[1][0] == p[2][0] or p[0][1] == p[1][1] and p[1][1] == p[2][1]:
     print(1)
     return
p.sort()
if p[0][0] == p[1][0]:
     print(3 if p[2][1] in range(min(p[0][1], p[1][1]) + 1, max(p[0][1], p[1][1])) else 2)
     return
if p[1][0] == p[2][0]:
     print(3 if p[0][1] in range(min(p[1][1], p[2][1]) + 1, max(p[1][1], p[2][1])) else 2)
     return
p = sorted((y, x) for (x, y) in p)
if p[0][0] == p[1][0]:
     print(3 if p[2][1] in range(min(p[0][1], p[1][1]) + 1, max(p[0][1], p[1][1])) else 2)
     return
if p[1][0] == p[2][0]:
     print(3 if p[0][1] in range(min(p[1][1], p[2][1]) + 1, max(p[1][1], p[2][1])) else 2)
     return
print(3)
