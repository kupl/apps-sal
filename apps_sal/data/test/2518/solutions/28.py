n, a, b = list(map(int, input().split()))
sh = sorted([int(input()) for i in range(n)], reverse=True)
sumh = sum(sh)


def nibu(t):
    rt = 0
    for i in range(n):
        temp = -1 * (-1 * max(0, sh[i] - t * b) // (a - b))
        if temp > 0:
            rt += temp
        else:
            break
        if rt > t:
            return False
    return True if t >= rt else False


l = max(sh) // a
r = max(sh) // b + 1
while r - l != 1:
    m = (l + r) // 2
    if nibu(m):
        r = m
    else:
        l = m
print(r)
