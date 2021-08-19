def codechef(s, x):
    flag = 0
    a = (s - x) // 2
    if (s - x) / 2 != a:
        print(0)
        return
    if s == x:
        flag = 1
    if a < 0:
        print(0)
        return
    a = str(bin(a))
    x = str(bin(x))
    a = a[2:]
    x = x[2:]
    l = len(a) - len(x)
    if l > 0:
        x = '0' * l + x
    else:
        a = '0' * -l + a
    res = 1
    for i in range(len(a)):
        if x[i] == '1' and a[i] == '0':
            res *= 2
        elif x[i] == '1' and a[i] == '1':
            print(0)
            return
    if flag:
        res -= 2
    print(res)


def __starting_point():
    (s, x) = list(map(int, input().split()))
    codechef(s, x)


__starting_point()
