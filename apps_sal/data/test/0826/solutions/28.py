n = int(input())


def f(k):
    return k * (k + 1) // 2


l = -1
r = n + 1
while r - l > 1:
    mid = l + (r - l) // 2

    if f(mid) <= n + 1:
        l = mid
    else:
        r = mid

ans = n - l + 1

print(ans)
