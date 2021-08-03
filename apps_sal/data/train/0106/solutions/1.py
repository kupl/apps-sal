def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


for _ in range(ii()):
    n = ii()
    a = [(li() + [i]) for i in range(n)]
    a.sort()
    ans = [2] * n
    pr = a[0][0]
    for l, r, i in a:
        if l > pr:
            break
        ans[i] = 1
        pr = max(pr, r)
    if 2 in ans:
        print(*ans)
    else:
        print(-1)
