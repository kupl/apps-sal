def one():
    return int(input())


def two():
    return list(map(int, input().split()))


def lis():
    return list(map(int, input().split()))


def st():
    return input()


for i in range(one()):
    input()
    d = {(0, 0): 0}
    s = st()
    c = [0, 0]
    r = 0
    m = float('inf')
    ans = None
    for j in s:
        if j == 'U':
            c[1] += 1
        if j == 'D':
            c[1] -= 1
        if j == 'R':
            c[0] += 1
        if j == 'L':
            c[0] -= 1
        r += 1
        if (c[0], c[1]) in d:
            if m > r - d[c[0], c[1]] + 1:
                ans = (d[c[0], c[1]] + 1, r)
                m = r - d[c[0], c[1]] + 1
            d[c[0], c[1]] = r
        else:
            d[c[0], c[1]] = r
    if not ans:
        print(-1)
    else:
        print(*ans)
