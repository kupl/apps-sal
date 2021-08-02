def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
a = li()
s = sum(a)
k = max(a)
while 1:
    if n * k - s > s:
        print(k)
        break
    k += 1
