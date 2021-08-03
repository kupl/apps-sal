def f(x1, y1, x2, y2):
    return x1 <= x2 <= y1 or x1 <= y2 <= y1 or x2 <= x1 <= y2


p, q, l, r = list(map(int, input().split()))
a1, a2 = [(0, 0)] * p, [(0, 0)] * q
for i in range(p):
    a, b = list(map(int, input().split()))
    a1[i] = (a, b)
for i in range(q):
    a, b = list(map(int, input().split()))
    a2[i] = (a, b)
res = [False] * 2000
ans = 0
for i in a1:
    for j in a2:
        for k in range(max(0, i[0] - j[1]), i[1] - j[0] + 1):
            res[k] = True
for i in range(l, r + 1):
    if res[i]:
        ans += 1
print(ans)
