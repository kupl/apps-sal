def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(mi())


n = ii()
c = sum(n % i == 0 for i in range(1, n))
print(c)
