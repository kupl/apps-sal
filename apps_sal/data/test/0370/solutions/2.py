K = int(input())
X, Y = [int(_) for _ in input().split()]
x, signx = abs(X), -1 if X < 0 else 1
y, signy = abs(Y), -1 if Y < 0 else 1
ans = [(x, y)]


def calcxy(x, y):
    dx = min(K, x)
    dy = K - dx
    x -= dx
    if y > dy:
        y -= dy
    else:
        y += dy
    return x, y


def calczw(x, y):
    # z+w=abs(z-x)+abs(w-y)=K
    if x > y:
        # z+w=x-z+w-y=K and z<=x and w>=y
        z = (x - y) // 2
        w = K - z
    else:
        # z+w=z-x+y-w=K and z>=x and w<=y
        w = (y - x) // 2
        z = K - w
    return (z, w)


if x + y != K:
    while (x + y) > 2 * K:
        x, y = calcxy(x, y)
        ans += [(x, y)]
    z, w = calczw(x, y)
    if abs(z - x) + abs(w - y) != K:
        x, y = calcxy(x, y)
        ans += [(x, y)]
        z, w = calczw(x, y)
    if abs(z - x) + abs(w - y) != K:
        print((-1))
        return
    ans += [(z, w)]
print((len(ans)))
for x, y in ans[::-1]:
    print((x * signx, y * signy))
