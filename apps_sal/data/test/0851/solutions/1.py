def check(p):
    cur = k - 2
    p += 1
    lastfree = 0
    lasteat = 0
    for i in range(1, n - 1):
        if tm[i] == '0':
            lastfree = i
        if i - lasteat >= p:
            if lasteat == lastfree or cur <= 0:
                return False
            lasteat = lastfree
            cur -= 1
    return True


def bs(l, r):
    while(l < r):
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1
    return l


n, k = map(int, input().split())
tm = input()

print(bs(0, n))
