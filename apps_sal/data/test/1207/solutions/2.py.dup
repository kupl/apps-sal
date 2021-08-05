n, m = [int(i) for i in input().split()]
n += 1  # one-indexed
A = [[int(i) for i in input().split()] for j in range(m)]
m += 1


def check(upper):
    p = [[] for i in range(n)]
    d = [0] * n  # record num of parents
    for u, v in A[:upper]:
        p[u].append(v)  # form arc from u to v
        d[v] += 1
    if d.count(0) > 2:
        return False
    x = d.index(0, 1)  # find the real ancestor, should only be one
    while x:
        q, x = p[x], 0
        for y in q:
            d[y] -= 1
            if d[y] == 0:
                if x:
                    return False
                x = y
    return True


left, right = 1, m
while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
if check(left):
    print(left)
else:
    print(-1)
