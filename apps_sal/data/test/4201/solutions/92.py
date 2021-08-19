h, w, k = list(map(int, input().split()))
c = [list(input()) for _ in range(h)]
ans = 0
for i in range(1 << h):
    for j in range(1 << w):
        cnt = sum(c[k][l] == '#' for k in range(h) for l in range(w) if (i >> k & 1) and (j >> l & 1))
        if cnt == k:
            ans += 1
print(ans)
