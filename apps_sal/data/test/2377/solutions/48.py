(n, h) = map(int, input().split())
(a, b) = ([], [])
for _ in range(n):
    (x, y) = map(int, input().split())
    a.append(x)
    b.append(y)
max_a = max(a)
b.sort(reverse=True)
cnt = 0
for i in range(n):
    if b[i] < max_a:
        break
    h -= b[i]
    cnt += 1
    if h <= 0:
        break
if h > 0:
    cnt += (h - 1) // max_a + 1
print(cnt)
