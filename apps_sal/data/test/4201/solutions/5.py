h, w, k = map(int, input().split())
m = [[] for _ in range(h)]
for y in range(h):
    m[y] = list(input())

ans = 0
for y in range(1 << h):
    for x in range(1 << w):
        cnt = 0
        for y2 in range(h):
            for x2 in range(w):
                if m[y2][x2] == '#' and y >> y2 & 1 and x >> x2 & 1:
                    cnt += 1
        if cnt == k:
            ans += 1
print(ans)
