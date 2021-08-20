(n, m) = map(int, input().split())
al = []
bl = []
for i in range(n):
    (a, b) = map(int, input().split())
    al.append([a, b])
for j in range(m):
    (c, d) = map(int, input().split())
    bl.append([c, d])


def check(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    return x + y


for a in al:
    min = 1000000000
    cnt = 1
    for b in bl:
        tmp = check(a, b)
        if tmp < min:
            ans = cnt
            min = tmp
        cnt += 1
    print(ans)
