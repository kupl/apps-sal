def mainA():
    n = int(input())
    s = input()
    cnt = 0
    for i in s:
        if i == '8':
            cnt += 1
    print(min(cnt, n // 11))


def mainB():

    def get(n):
        ret = 0
        while n > 0:
            ret += n % 10
            n //= 10
        return ret
    n = int(input())
    if n <= 9:
        print(n)
        return
    t = 9
    while n > t:
        t = t * 10 + 9
    t //= 10
    print(get(t) + get(n - t))


mainB()
