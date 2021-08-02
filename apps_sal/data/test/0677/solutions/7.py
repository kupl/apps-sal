def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


for _ in range(ii()):
    l, r, d = mi()
    ans = d
    if l <= d <= r:
        ans = d * (r // d + 1)
    print(ans)
