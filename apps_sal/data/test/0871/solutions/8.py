n, s = map(int, input().split())
t = []
for i in range(n):
    h, m = map(int, input().split())
    t.append(60 * h + m)
x, y = 0, 0
if t[0] < s + 1:
    for i in range(n - 1):
        if t[i + 1] - t[i] >= 2 * s + 2:
            x = t[i] + s + 1
            break
    if x == 0:
        x = t[n - 1] + s + 1
y = x % 60
x = x // 60
print(x, y)
