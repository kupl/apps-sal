n = int(input())
x = [int(x) for x in input().strip().split(' ')]
v = [int(x) for x in input().strip().split(' ')]
p = 0
q = 1.0 * (max(x) - min(x)) / min(v)


def verify(t):
    span = [-M, M]
    for i in range(n):
        tmp = (x[i] - v[i] * t, x[i] + v[i] * t)
        if tmp[0] > span[1] or tmp[1] < span[0]:
            return []
        span = [max(span[0], tmp[0]), min(span[1], tmp[1])]
    return span


M = max(x)
while p < q - 1e-07:
    m = p + (q - p) / 2
    span = verify(m)
    if len(span) > 0:
        q = m
    else:
        p = m
print(p)
