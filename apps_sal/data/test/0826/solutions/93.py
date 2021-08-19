def sigma1(n):
    return n * (n + 1) // 2


n = int(input())


def do():
    l = 0
    h = n
    while l <= h:
        mid = (l + h) // 2
        if sigma1(mid) <= n + 1:
            l = mid + 1
        else:
            h = mid - 1
    return h if sigma1(h) <= n + 1 else l


x = do()
print(1 + (n - do()))
