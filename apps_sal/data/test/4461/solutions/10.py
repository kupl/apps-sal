H, W = map(int, input().split())


def abc(x, y, z):  # x,y:高さまたは幅、z:ｙの幅をもつピースの高さ
    a = z * y
    if (x - z) & 1 and y & 1:
        b = max(x - z, y) // 2 * min(x - z, y)
        c = x * y - a - b
    else:
        b = c = (x - z) * y // 2
    return a, b, c


def diffS(a, b, c):  # a,b,c:abc()の戻り値
    return max(a, b, c) - min(a, b, c)


def solve(x, y):  # x,y:高さまたは幅
    z = x // 3
    return min(diffS(*abc(x, y, z)), diffS(*abc(x, y, z + 1)))


if H % 3 == 0 or W % 3 == 0:
    ans = 0
else:
    ans = min(solve(H, W), solve(W, H))
print(ans)
