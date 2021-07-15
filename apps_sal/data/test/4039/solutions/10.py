n, r = map(int, input().split())
 
pt = []
nt = []
r2 = r
for _ in range(n):
    a, b = map(int, input().split())
    r2 += b
    if b >= 0:
        pt.append((a, b))
    else:
        nt.append((a, b))
 
if r2 < 0:
    print('NO')
    return
 
pt.sort()
nt.sort(key=lambda t: t[0]+t[1])
 
for a, b in pt:
    if r<a:
        print("NO")
        return
    r += b
 
for a, b in nt:
    if r2 < a+b:
        print('NO')
        return
    r2 -= b
 
print('YES')
