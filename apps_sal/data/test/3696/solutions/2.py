def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

n = ii()
def gen(p, q, r):
    x = [0, p]
    y = [q]
    for c in range(1, n):
        
        nx = [0] + [-xi for xi in x]
        px = [0] + x
        if r: nx, px = px, nx
        
        bad = 0
        for i in range(len(y)):
            px[i] += y[i]
            if abs(px[i]) > 1:
                bad = 1
                break
        if not bad:
            x, y = px, x
            continue
        
        bad = 0
        for i in range(len(y)):
            nx[i] += y[i]
            if abs(nx[i]) > 1:
                bad = 1
                break
        if not bad:
            x, y = nx, x
            continue
        
        print('OH NO')
        z = 1 / 0
    return x, y

found = 0
for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
    for r in [0, 1]:
        x, y = gen(i, j, r)
        #print(x, y)
        if x[-1]==1 and y[-1]==1:
            found = 1
            break
    if found: break
if not found:
    print(n, 'OH NO!!')
print(len(x)-1)
print(*x)
print(len(y)-1)
print(*y)

