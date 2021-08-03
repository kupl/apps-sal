n, s = map(int, input().split())
a = []
for _ in range(n):
    h, m = map(int, input().split())
    a.append((h, m))
b = [h * 60 + m for (h, m) in a]
c = -1
if b[0] > s:
    print(0, 0)
else:
    for i in range(n - 1):
        if b[i + 1] - b[i] > s * 2 + 1:
            c = i
            break
    r = ((b[c] + s + 1) // 60, (b[c] + s + 1) % 60)
    print(r[0], r[1])
