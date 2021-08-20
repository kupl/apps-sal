n = int(input())
inf = 10 ** 6
abc = [inf] * 7
u = []


def rf(x, y):
    if x > y:
        return y
    return x


for i in range(n):
    (k, s) = input().split()
    k = int(k)
    s = list(s)
    s.sort()
    a = 'A' in s
    b = 'B' in s
    c = 'C' in s
    if a:
        abc[0] = rf(abc[0], k)
    if b:
        abc[1] = rf(abc[1], k)
    if c:
        abc[2] = rf(abc[2], k)
    if a and b:
        abc[3] = rf(abc[3], k)
    if c and b:
        abc[4] = rf(abc[4], k)
    if a and c:
        abc[5] = rf(abc[5], k)
    if a and b and c:
        abc[6] = rf(abc[6], k)
a1 = [0] * 5
a1[0] = abc[0] + abc[1] + abc[2]
a1[1] = abc[0] + abc[4]
a1[2] = abc[1] + abc[5]
a1[3] = abc[2] + abc[3]
a1[4] = abc[6]
ans = min(a1)
if ans == inf:
    print(-1)
else:
    print(ans)
