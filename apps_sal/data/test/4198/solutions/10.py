a, b, x = map(int, input().split())


def f(n):
    return x - (n * a + b * len(str(n)))


def test(n):
    if f(n) >= 0:
        return True
    else:
        return False


l = 0
r = 10**9
flag = True

while flag:
    mid = (r + l) // 2
    if test(mid):
        l = mid
    else:
        r = mid
    if r - l <= 1:
        flag = False
        if test(r) and test(l):
            print(r)
        elif test(r) and test(l) != True:
            print(r)
        else:
            print(l)
