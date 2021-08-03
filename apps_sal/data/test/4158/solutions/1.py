def f():
    k = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    d = {}
    for i, j in enumerate(l):
        d[j] = i
    n = 1
    s = ''
    while l[0] + n <= l[-1]:
        for i in l:
            if i + n in d and i + 2 * n in d:
                print(3)
                print(i, i + n, i + 2 * n)
                return
            elif i + n in d:
                s = str(i) + ' ' + str(i + n)
        n = n * 2
    if s == '':
        print(1, l[0], sep='\n')
    else:
        print(2, s, sep='\n')


f()
