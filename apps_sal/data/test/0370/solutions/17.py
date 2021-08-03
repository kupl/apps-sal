K = int(input())
X, Y = map(int, input().split())

ans = [(X, Y)]
x, y = ans[-1]
while abs(x) >= 3 * K // 2:
    x, y = ans[-1]
    if x >= K:
        x -= K
    elif x <= -K:
        x += K
    ans.append((x, y))
dx = abs(x)

while abs(y) > 2 * K - dx:
    x, y = ans[-1]
    if y > 0:
        y -= K
    else:
        y += K
    ans.append((x, y))

x, y = ans[-1]
if abs(y) + abs(x) != K:
    if (x + y) % 2 == 0 and K % 2 == 0:
        d2 = (abs(x) + abs(y)) // 2
        if abs(x) > abs(y):
            x -= d2 * (1 if x > 0 else -1)
            y += (K - d2) * (1 if y > 0 else -1)
        else:
            x += (K - d2) * (1 if x > 0 else -1)
            y -= d2 * (1 if y > 0 else -1)
        ans.append((x, y))
    else:
        if (x + y + K) % 2 == 0:
            y -= K if y > 0 else (-K)
            ans.append((x, y))
        d = abs(x) + abs(y)
        if abs(x) > abs(y):
            x -= d // 2 * (1 if x > 0 else -1)
            y += (K - d // 2) * (1 if y > 0 else -1)
        else:
            x += (K - d // 2) * (1 if x > 0 else -1)
            y -= d // 2 * (1 if y > 0 else -1)
        ans.append((x, y))
x, y = ans[-1]

if abs(x) + abs(y) != K:
    print(-1)
else:
    ans = ans[::-1]
    print(len(ans))
    for out in ans:
        print(*out)
