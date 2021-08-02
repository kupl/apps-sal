def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n, k = mi()

y = min(n, k - 1)
x = k - y
ans = 0
if x < y:
    dif = y - x
    ans = (dif + 1) // 2
print(ans)
