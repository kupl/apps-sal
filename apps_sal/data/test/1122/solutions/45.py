n, m = list(map(int, input().split()))


def ark(a, b):
    return min(abs(a - b), n - abs(a - b))


a, b = n, 1
S = set()
for i in range(m):
    if 2 * ark(a, b) == n or ark(a, b) in S:
        a -= 1
    print((a, b))
    S.add(ark(a, b))
    a -= 1
    b += 1
