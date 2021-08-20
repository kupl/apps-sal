(n, m) = map(int, input().split())
p = []
v = []
for i in range(n):
    p.append(input())
r = 0
for i in range(m):
    v.append(input())
    if v[-1] in p:
        del p[p.index(v[-1])]
        del v[-1]
        r += 1
print('YES' if r % 2 and len(p) >= len(v) or (r % 2 == 0 and len(p) > len(v)) else 'NO')
