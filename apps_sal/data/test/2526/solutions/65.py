(X, Y, A, B, C) = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
ans = sum(p[:X]) + sum(q[:Y])
x = X - 1
y = Y - 1
m = min(p[x], q[y])
n = 1
while len(r) > 0 and r[0] > m:
    if n == 1:
        if p[x] > q[y]:
            ans += r[0] - q[y]
            y -= 1
        else:
            ans += r[0] - p[x]
            x -= 1
    else:
        ans += r[0] - m
        if x < 0:
            y -= 1
        else:
            x -= 1
    r.pop(0)
    if y >= 0 and x >= 0:
        m = min(p[x], q[y])
    elif x >= 0 and y < 0:
        m = p[x]
        n = 0
    elif y >= 0 and x < 0:
        m = q[y]
        n = 0
    else:
        m = 10 ** 9 + 1
        n = 0
print(ans)
