def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


# M. The Pleasant Walk
n, k = mi()
a = li()
c = p = 0
ans = 1
for ai in a:
    if ai == p:
        c = 1
    else:
        c += 1
        ans = max(ans, c)
    p = ai
print(ans)
