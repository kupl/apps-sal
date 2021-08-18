X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

x = X - 1
y = Y - 1

p = sorted(p, reverse=True)
q = sorted(q, reverse=True)
r = sorted(r, reverse=True)


if p[x] >= q[y]:
    a = q[y]
    f = 1
else:
    a = p[x]
    f = 2
while len(r) >= 1 and a < r[0]:
    if f == 1:
        q[y] = r[0]
        y -= 1
        r.pop(0)
    elif f == 2:
        p[x] = r[0]
        x -= 1
        r.pop(0)
    else:
        break

    if (y == -1 and x >= 0) or (x >= 0 and p[x] < q[y]):
        a = p[x]
        f = 2
    elif (x == -1 and y >= 0) or (y >= 0 and p[x] >= q[y]):
        a = q[y]
        f = 1
    else:
        break

ans = 0
for i in p[:X]:
    ans += i
for i in q[:Y]:
    ans += i

print(ans)
