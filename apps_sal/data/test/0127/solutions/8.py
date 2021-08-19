(n, f) = list(map(int, input().split()))
r = []
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    if 2 * a <= b:
        r.append((a, a))
    elif a <= b:
        r.append((b - a, a))
    else:
        r.append((0, b))
ret = 0
r1 = sorted(r)[::-1]
for (a, b) in r1[:f]:
    ret += a + b
for (a, b) in r1[f:]:
    ret += b
print(ret)
