x = int(input())


def prime_check(n):
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        else:
            f += 2
    else:
        return True


if x != 2:
    if x % 2 == 0:
        x += 1
    while 1:
        if prime_check(x) == True:
            print(x)
            break
        else:
            x += 2
else:
    print(2)
