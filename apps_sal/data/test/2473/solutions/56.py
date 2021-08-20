(n, k) = map(int, input().split())
li = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: (x[1], x[0]))
ans = float('INF')
for i in range(n):
    for j in range(i + 1, n):
        (ux, lx) = (max(li[i][0], li[j][0]), min(li[i][0], li[j][0]))
        (l, r) = (0, 0)
        cnt = int(lx <= li[r][0] <= ux)
        while True:
            while r < n - 1 and cnt < k:
                r += 1
                cnt += int(lx <= li[r][0] <= ux)
            if cnt < k or not 0 <= r <= n - 1 or (not 0 <= l <= n - 1) or (r <= l):
                break
            if ans > (ux - lx) * (li[r][1] - li[l][1]):
                ans = (ux - lx) * (li[r][1] - li[l][1])
            cnt -= int(lx <= li[l][0] <= ux)
            l += 1
print(ans)
