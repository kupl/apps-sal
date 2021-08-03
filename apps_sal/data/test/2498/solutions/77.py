n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

for i in range(n):
    a[i] = a[i] // 2


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def check(x):
    cnt = 0
    while(1):
        if x % 2 == 0:
            x = x // 2
            cnt += 1
        else:
            break
    return cnt


cnt = a[0]
for i in range(n):
    cnt = lcm(cnt, a[i])


l = check(a[0])
for i in range(1, n):
    x = check(a[i])
    if x != l:
        print((0))
        return


s = m // cnt
if s % 2 == 0:
    print((s // 2))
else:
    print((s // 2 + 1))
