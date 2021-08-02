n, k = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(n)]
l.sort()
l1 = sorted(l, key=lambda x: x[1])
ans = float("INF")

for i in l:
    for j in l:
        if i[0] >= j[0]:
            continue
        for s in l1:
            count = 0
            for w, h in l1:
                if i[0] <= w <= j[0] and s[1] <= h:
                    count += 1
                if count == k:
                    ans = (min(ans, (j[0] - i[0]) * (h - s[1])))
                    break

print(ans)
