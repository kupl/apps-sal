n = int(input())
xs = list([len(list(x)) + 1 for x in input().replace('-', ' ').split()])
xs[-1] -= 1


def f(xs, n, c):
    cnt = 1
    tmp = 0
    for x in xs:
        if c < x:
            return False
        elif c < tmp + x:
            tmp = 0
            cnt += 1
        tmp += x
    return cnt <= n


l = 1
r = sum(xs)

while l + 1 < r:
    c = (l + r) // 2
    if f(xs, n, c):
        r = c
    else:
        l = c

print(r)
