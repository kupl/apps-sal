t = int(input())
for i in range(t):
    n, m = [int(x) for x in input().split(' ')]
    alist = [int(x) for x in input().split(' ')]
    blist = alist[:]
    if (n == 2) or (m < n):
        print('-1')
    else:
        alist.remove(min(alist))
        print(2 * sum(blist) + (m - n) * (min(blist) + min(alist)))
        for i in range(n - 1):
            print(i + 1, i + 2, sep=' ')
        print(n, 1, sep=' ')
        a = blist.index(min(blist))
        b = alist.index(min(alist))
        if b >= a:
            for i in range(m - n):
                print(a + 1, b + 2, sep=' ')
        else:
            for i in range(m - n):
                print(b + 1, a + 1, sep=' ')
