xy = [0, 0]


def check(k):
    nonlocal xy
    x, y = xy
    got = True
    if y * 2 > k:
        y -= k // 2
        if k % 2 != 0:
            if x != 0:
                x -= 1
            elif y != 0:
                y -= 1
            else:
                got = False
    else:
        k -= y * 2
        y = 0
        if k <= x:
            x -= k
        else:
            got = False
    xy = [x, y]
    return got


n, y, x = map(int, input().split())
k = sorted(map(int, input().split()))
cnt = 0
xy = [x, y]
while cnt < n and check(k[cnt]):
    cnt += 1
print(cnt)
