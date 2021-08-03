def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


MX = 10 ** 5

n = ii()
if n % 2 == 0:
    ans = n // 2
else:
    c = 3
    ans = 0
    while c <= MX:
        if n % c == 0:
            n -= c
            ans += 1
            break
        c += 1
    if ans:
        ans += n // 2
    else:
        ans = 1
print(ans)
