def check(k, n, dx, dy):
    x = (k // n) * px[n]
    y = (k // n) * py[n]
    x += px[k % n]
    y += py[k % n]
    if abs(x - dx) + abs(y - dy) <= k:
        return 1
    return 0


x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
dx = x2 - x1
dy = y2 - y1
n = int(input())
s = input()
px = [0] * (n + 5)
py = [0] * (n + 5)
for i in range(1, n + 1):
    px[i] = px[i - 1]
    py[i] = py[i - 1]
    if s[i - 1] == 'U':
        py[i] += 1
    elif s[i - 1] == 'D':
        py[i] -= 1
    elif s[i - 1] == 'L':
        px[i] -= 1
    else:
        px[i] += 1


s = 0
e = int(10**18)
ans = -1

while s <= e:
    m = (s + e) // 2
    if check(m, n, dx, dy):
        ans = m
        e = m - 1
    else:
        s = m + 1
print(ans)
