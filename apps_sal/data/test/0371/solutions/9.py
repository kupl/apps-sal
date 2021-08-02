N = int(2e5)
n = int(input())
cb = [x * x * x for x in range(2, N)]


def valid(m):
    return sum(m // i for i in cb) < n


def binary_search():
    l, r = 0, int(1e16)
    while l < r:
        m = (l + r) // 2
        if valid(m):
            l = m + 1
        else:
            r = m
    return l


res = binary_search()
print(res if sum(res // i for i in cb) == n else -1)
