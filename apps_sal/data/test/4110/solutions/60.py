d, g = map(int, input().split())
p, c = [], []
ans = 1 << 32
for i in range(d):
    x, y = map(int, input().split())
    p.append(x)
    c.append(y)
for i in range(1 << d):
    cnt = 0
    tmp = 0
    for j in range(d):
        if i & (1 << j):
            tmp += (j + 1) * 100 * p[j] + c[j]
            cnt += p[j]
    if tmp < g:
        for j in range(d - 1, -1, -1):
            if i & (1 << j) == 0:
                for k in range(p[j]):
                    if tmp >= g:
                        break
                    tmp += (j + 1) * 100
                    cnt += 1
                else:
                    tmp += c[j]
    ans = min(cnt, ans)
print(ans)
