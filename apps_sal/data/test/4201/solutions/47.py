h, w, k = map(int, input().split())
c = [input() for _ in range(h)]

ans = 0
for i in range(1 << h):
    for j in range(1 << w):
        t = 0
        for a in range(h):
            for b in range(w):
                if (i >> a) & 1 and (j >> b) & 1 and c[a][b] == "#": t += 1
        if t == k: ans += 1
print(ans)
