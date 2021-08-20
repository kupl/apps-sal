from collections import Counter
(h, w, n) = list(map(int, input().split()))
c = Counter([])
for i in range(n):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    for i in range(-2, 1):
        for j in range(-2, 1):
            if 0 <= a + i < h - 2 and 0 <= b + j < w - 2:
                c[a + i, b + j] += 1
ans = [0] * 10
total = 0
for (k, v) in list(c.items()):
    ans[v] += 1
    total += 1
ans[0] = (h - 2) * (w - 2) - total
for a in ans:
    print(a)
