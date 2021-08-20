def cc(res):
    l = 1
    r = res
    while l <= r:
        mid = l + r >> 1
        if mid * mid == res:
            return mid
        elif mid * mid > res:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def solve(a, b, c):
    if b * b - 4 * a * c < 0:
        return -1
    r = cc(b * b - 4 * a * c)
    if r * r != b * b - 4 * a * c:
        return -1
    r = -b + r
    if r % (2 * a) != 0:
        return -1
    return int(r / 2 / a)


n = int(input())
tmp = []
for i in range(0, 100):
    now = 1 << i + 1
    ans = solve(1, now - 3, -2 * n)
    if ans != -1 and ans % 2 == 1:
        tmp.append(int(ans * now / 2))
tmp.sort()
pre = -1
for i in tmp:
    if i != pre:
        print(i)
    pre = i
if pre == -1:
    print(-1)
