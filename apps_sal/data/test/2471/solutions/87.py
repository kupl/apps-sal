h, w, n = map(int, input().split())
cnt = {}

for _ in range(n):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 < a + i < h - 1 and 0 < b + j < w - 1:
                if (a + i, b + j) not in cnt:
                    cnt[(a + i, b + j)] = 0
                cnt[(a + i, b + j)] += 1

ans = {i: 0 for i in range(10)}
ans[0] = (h - 2) * (w - 2)
for _, x in cnt.items():
    ans[x] += 1
    ans[0] -= 1

for i in range(10):
    print(ans[i])
