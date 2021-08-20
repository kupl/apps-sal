def cnt(x1, y1, x2, y2):
    ans = 0
    for i in range(y2, y1 + 1):
        for j in range(x1, x2 + 1):
            if lst[i][j] == 1:
                ans += 1
    return ans


(h, w, n, kk) = list(map(int, input().split()))
anss = 0
lst = [[0] * 20 for i in range(20)]
for i in range(n):
    (x, y) = list(map(int, input().split()))
    lst[x - 1][y - 1] = 1
for i in range(h):
    for j in range(w):
        for k in range(h):
            for z in range(w):
                if cnt(j, i, z, k) >= kk:
                    anss += 1
print(anss)
