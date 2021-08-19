from collections import Counter
(H, W, N) = list(map(int, input().split()))
dir = [[0, 0], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
dict = {}
for i in range(N):
    (a, b) = list(map(int, input().split()))
    for (dy, dx) in dir:
        if 2 <= a + dy <= H - 1 and 2 <= b + dx <= W - 1:
            if (a + dy, b + dx) not in dict:
                dict[a + dy, b + dx] = 1
            else:
                dict[a + dy, b + dx] += 1
c = Counter(list(dict.values()))
ans = [0 for _ in range(10)]
for (k, v) in list(c.items()):
    if v > 0:
        ans[k] = v
ans[0] = (H - 2) * (W - 2) - sum(ans[1:])
for i in range(10):
    print(ans[i])
