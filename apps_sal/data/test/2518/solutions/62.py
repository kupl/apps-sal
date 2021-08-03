N, A, B = map(int, input().split())
hs = [int(input()) for _ in range(N)]
l = 0
r = max(hs)


def enough(x):
    res = 0
    for i in range(N):
        res += max(0, (hs[i] - B * x + A - B - 1)) // (A - B)
    return res <= x


while l + 1 < r:
    m = (l + r) // 2
    if enough(m):
        r = m
    else:
        l = m

print(r)
