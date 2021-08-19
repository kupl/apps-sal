(w, h, n) = list(map(int, input().split()))
ans = [[0 for _ in range(w)] for _ in range(h)]
for i in range(n):
    (x, y, a) = list(map(int, input().split()))
    if a == 1:
        for j in range(h):
            ans[j][:x] = [1 for _ in range(x)]
    if a == 2:
        for j in range(h):
            ans[j][x:] = [1 for _ in range(w - x)]
    if a == 3:
        for j in range(h - y, h):
            ans[j] = [1 for _ in range(w)]
    if a == 4:
        for j in range(h - y):
            ans[j] = [1 for _ in range(w)]
cnt = 0
for k in ans:
    cnt += k.count(0)
print(cnt)
