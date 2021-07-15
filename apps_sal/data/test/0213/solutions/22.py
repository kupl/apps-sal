import math

def f(m):
    nonlocal h
    f = True
    for i in range(len(h)):
        for j in h[i]:
            if not(j <= i * m and j > (i - 1) * m ):
                f = False
    return f

n, m = map(int, input().split())
h  = [[] for i in range(110)]
for i in range(m):
    a, b = map(int, input().split())
    h[b].append(a)
k = 0
ans = []
for i in range(1, 110):
    if f(i):
        k += 1
        ans.append(i)
fl = False
for i in range(len(h)):
    for j in h[i]:
        if j == n:
            fl = True
            ans1 = i
if fl:
    print(ans1)
elif m == 0 and n == 1:
    print(1)
elif k > 1:
    pr = math.ceil(n / ans[0])
    fl1 = True
    for i in range(1, len(ans)):
        if pr != math.ceil(n / ans[i]):
            fl1 = False
    if not fl1:
        print(-1)
    else:
        print(pr)
elif k < 1:
    print(-1)
else:
    print(math.ceil(n / ans[0]))
