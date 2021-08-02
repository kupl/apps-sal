N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]


def parity():
    res = sum(xy[0]) % 2
    for x, y in xy:
        if (x + y) % 2 != res:
            return -1
    return res


p = parity()
if p == -1:
    print(-1)
    return

dd = [1]
if p == 0: dd.append(1)
lim = 10**12
while len(dd) < 40 and dd[-1] * 2 <= lim:
    dd.append(dd[-1] * 2)
print(40)
print(*dd)

for x, y in xy:
    ans = ""
    for d in dd[::-1]:
        if abs(x) > abs(y):
            if x > 0:
                x -= d
                ans += "R"
            else:
                x += d
                ans += "L"
        else:
            if y > 0:
                y -= d
                ans += "U"
            else:
                y += d
                ans += "D"
    print(ans[::-1])
