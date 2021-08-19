from collections import Counter
(h, w, N) = map(int, input().split())
rec = []
for i in range(N):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    for i in range(-2, 1):
        for j in range(-2, 1):
            if 0 <= a + i < h - 2 and 0 <= b + j < w - 2:
                rec.append((a + i, b + j))
ans = [0] * 10
ans[0] = (h - 2) * (w - 2)
c = Counter(rec)
for i in c.values():
    ans[i] += 1
    ans[0] -= 1
for i in range(10):
    print(ans[i])
