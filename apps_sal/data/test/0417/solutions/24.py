from operator import itemgetter

n, x, d = map(int, input().split())

if d == 0:
    if x == 0:
        print(1)
    else:
        print(n+1)
    return
if d < 0:
    x *= -1
    d *= -1

p = dict()
q = dict()

for k in range(n+1):
    temp = k * x % d
    if temp in p.keys():
        #print((k - p[temp]) * x)
        a = (k - p[temp]) * x // d
        L = (k-1)*k//2 + a
        H = (2*n-k-1)*k//2 + a
        q[temp].append([L, H])
    else:
        p[temp] = k
        L = (k-1)*k//2
        H = (2*n-k-1)*k//2
        q[temp] = [[L, H]]

ans = 0

for z in q.values():
    c = - float('inf')
    for a, b in sorted(z):
        if a > c:
            ans += b - a + 1
        elif b > c:
            ans += b - c
        else:
            continue
        c = b

print(ans)
