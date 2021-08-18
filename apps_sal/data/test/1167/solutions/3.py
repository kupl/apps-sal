
def rint():
    return int(input())


def rints():
    return list(map(int, input().split()))


t = rint()
for _ in range(t):
    a, b, c, d, k = rints()
    x = (a + c - 1) // c
    y = (b + d - 1) // d
    if x + y > k:
        print(-1)
    else:
        print(x, y)
