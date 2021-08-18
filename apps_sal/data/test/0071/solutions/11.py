n, m, k, x, y = map(int, input().split(" "))


def s(row, col):
    ret = 0
    if (l % 2 == 0):
        if(row == n or row == 1):
            ret = l // 2
        else:
            ret = l
        if (rl >= row or (rl + 1 == row and col <= rr)):
            ret += 1
    else:
        if(row == n):
            ret = (l - 1) // 2
        elif (row == 1):
            ret = (l + 1) // 2
        else:
            ret = l
        if (n - rl < row or (n - rl == row and col <= rr)):
            ret += 1
    return ret


if n == 1:
    r = k // m

    rr = k % m

    if (rr > 0):
        maxi = r + 1
    else:
        maxi = r
    mini = r
    if y <= rr:
        sergei = r + 1
    else:
        sergei = r
else:
    r = k // m

    rr = k % m

    l = r // (n - 1)

    rl = r % (n - 1)

    if l % 2 == 0:
        maxi = max(s(2, 1), s(1, 1))
        mini = s(n, 1)
    else:
        maxi = max(s(n - 1, 1), s(1, 1))
        mini = s(n, m)
    sergei = s(x, y)

print(maxi, mini, sergei)
