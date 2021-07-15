from collections import Counter
N = int(input())
if N == 2:
    print(0)
    return
inf = 10**9+7
inf2 = 10**18
def gcdl(A):
    if len(A) == 0:
        return -1
    if len(A) == 1:
        return 0
    g = gcd(A[0], A[1])
    for a in A[2:]:
        g = gcd(a, g)
    return g
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
Point = []
ans = 0
for _ in range(N):
    Point.append(list(map(int, input().split())))
S = Counter()
T = set()
for i in range(N):
    x1 , y1 = Point[i]
    for j in range(N):
        if i == j:
            continue
        x2 , y2 = Point[j]
        a = y1 - y2
        b = -(x1 - x2)
        c = x2*y1 - x1*y2
        g = gcdl([a, b, c])
        a //= g
        b //= g
        c //= g
        if a < 0:
            a *= -1
            b *= -1
            c *= -1
        k = a*inf+b*inf2+c
        if k not in T:
            T.add(a*inf+b*inf2+c)
            if x1 == x2:
                S[-1] += 1
            else:
                y = y1 - y2
                x = x1 - x2
                g = gcd(y, x)
                y //= g
                x //= g
                if y < 0:
                    y *= -1
                    x *= -1
                S[y*inf+x] += 1
L = len(T)
ans = L*(L-1)//2
for s in S.values():
    ans -= s*(s-1)//2
print(ans)
