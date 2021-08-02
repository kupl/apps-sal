def s():
    n = int(input())

    def st(x):
        if x[0] == ':':
            x = x[1:]
        if x[-1] == ':':
            x = x[:-1]
        return x
    for _ in range(n):
        a = st(input()).split(':')
        for i in range(len(a)):
            if len(a[i]) == 0:
                a[i] = '0000:' * (8 - len(a)) + '0000'
            elif len(a[i]) < 4:
                a[i] = '0' * (4 - len(a[i])) + a[i]
        print(*a, sep=':')


s()
