n, m = map(int, input().split())
xvis = [False] * (n + 1)
yvis = [False] * (n + 1)
xc = 0
yc = 0


def cal():
    s = (n - xc) * n - (n - xc) * yc
    return s


for i in range(m):
    x, y = map(int, input().split())
    if not(xvis[x]):
        xvis[x] = True
        xc += 1
    if not(yvis[y]):
        yvis[y] = True
        yc += 1
    print(cal(), end=' ')
