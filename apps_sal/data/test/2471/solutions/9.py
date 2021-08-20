from collections import Counter
(h, w, n) = map(int, input().split())
black_count = {}
for _ in range(n):
    (a, b) = map(int, input().split())
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            y = a + dy
            x = b + dx
            if 2 <= y <= h - 1 and 2 <= x <= w - 1:
                black_count[y, x] = black_count.get((y, x), 0) + 1
ans = Counter(black_count.values())
ans[0] = (h - 2) * (w - 2) - sum(ans.values())
for i in range(10):
    print(ans.get(i, 0))
