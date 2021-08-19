n = int(input())


def zrs(n):
    ret = 0
    while n >= 5:
        n //= 5
        ret += n
    return ret


def bins(n):
    (a, b) = (1, n * 5 + 1)
    while a < b:
        mid = (a + b) // 2
        guess = zrs(mid)
        if guess < n:
            a = mid + 1
        elif guess > n:
            b = mid - 1
        else:
            return mid
    return 0


x = bins(n)
x = x - x % 5
if x == 0:
    print('0')
else:
    print('5')
    print(' '.join(map(str, list(range(x, x + 5)))))
