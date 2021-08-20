(d, g) = map(int, input().split())
(p, c) = ([], [])
ans = float('inf')
for i in range(d):
    (x, y) = map(int, input().split())
    p.append(x)
    c.append(y)
for i in range(1 << d):
    (tmp, cnt) = (0, 0)
    for j in range(d):
        if i & 1 << j:
            tmp = tmp + 100 * (j + 1) * p[j] + c[j]
            cnt += p[j]
    if tmp >= g:
        if cnt < ans:
            ans = cnt
    else:
        for j in range(d - 1, -1, -1):
            if i & 1 << j:
                continue
            for k in range(p[j]):
                if tmp >= g:
                    break
                tmp = tmp + 100 * (j + 1)
                cnt += 1
        if cnt < ans:
            ans = cnt
print(ans)
