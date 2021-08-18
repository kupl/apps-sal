n, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

v = n - 1
h = n - 1
tate = [n - 1] * n
yoko = [n - 1] * n
ans = (n - 2)**2
for q1, q2 in queries:
    q2 -= 1
    if q1 == 1:
        if q2 < h:
            ans -= v - 1
            for i in range(h, q2, -1):
                tate[i] = v
            h = q2
        else:
            ans -= tate[q2] - 1
    else:
        if q2 < v:
            ans -= max(0, h - 1)
            for i in range(v, q2, -1):
                yoko[i] = h
            v = q2
        else:
            ans -= yoko[q2] - 1
print(ans)
