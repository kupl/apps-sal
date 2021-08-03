t = int(input())


def fun(n):
    ans = 0
    two = 0
    three = 0
    while n % 2 == 0:
        n /= 2
        two += 1
    while n % 3 == 0:
        n /= 3
        three += 1
    if n != 1:
        print(-1)
    else:
        if two > three:
            print(-1)
        else:
            print(2 * three - two)


while t:
    t -= 1
    n = int(input())
    fun(n)
