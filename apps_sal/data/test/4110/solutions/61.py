d, g = map(int, input().split())
T = []
for _ in range(d):
    p, c = map(int, input().split())
    T.append([p, c])

ans = float('inf')
for i in range(1 << d):
    Q = []
    cnt = 0
    score = 0
    for j in range(d):
        if (i >> j) & 1:
            Q.append(j)
    for v in Q:
        score += 100 * (v + 1) * (T[v][0]) + T[v][1]
        cnt += T[v][0]
    if score >= g:
        ans = min(ans, cnt)
    else:
        for i in range(d - 1, -1, -1):
            if i in Q:
                continue
            if score >= g:
                continue
            rest = T[i][0]
            while rest:
                if score >= g:
                    break
                score += 100 * (i + 1)
                rest -= 1
                cnt += 1
        ans = min(ans, cnt)
print(ans)
