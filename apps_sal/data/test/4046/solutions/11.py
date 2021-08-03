n = int(input())
q = list(map(int, input().split()))
p = list(range(n))
p[0] = 0
minp = 0
for i in range(1, n):
    p[i] = q[i - 1] + p[i - 1]
    if p[i] < minp:
        minp = p[i]
minp = -minp
for i in range(n):
    p[i] += minp + 1
sp = sorted(p)
if sp[0] != 1:
    print(-1)
else:
    fail = 0
    for i in range(1, n):
        if sp[i] != sp[i - 1] + 1:
            fail = 1
            break
    if fail:
        print(-1)
    else:
        print(*p)
