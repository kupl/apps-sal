n = int(input())
s = ' ' + input()

r = [(0, 0)]
for i in range(1, n + 1):
    x, y = r[i - 1]
    if s[i] == "U": y += 1
    if s[i] == "D": y -= 1
    if s[i] == "L": x -= 1
    if s[i] == "R": x += 1
    r += [(x, y)]
ans = 0
for i in range(1, n):
    for j in range(i + 1, n + 1):
        if (0, 0) == (r[j][0] - r[i - 1][0], r[j][1] - r[i - 1][1]): ans += 1
print(ans)
