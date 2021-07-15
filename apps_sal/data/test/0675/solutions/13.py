m, t, r = map(int, input().split())
if t < r:
    print(-1)
    return
w, l, v = list(map(int, input().split())), [r] * m, 0
for i in range(m):
    for j in range(l[i]):
        v += 1
        for k in range(i + 1, m):
            if w[i] - j - 1 + t < w[k]:
                break
            l[k] -= 1
print(v)
