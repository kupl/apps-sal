n = int(input())

if n == 1 or n == 2:
    print(1)
    return


def cut(n):
    l = 0
    r = n
    while r - l > 1:
        mid = (l + r) // 2
        if mid * (mid + 1) // 2 <= (n + 1):
            l = mid
        else:
            r = mid
    return l


print(n - cut(n) + 1)
