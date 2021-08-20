def main2():
    (n, x) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    a.sort()
    count = 9999
    for i in range(len(a) - 1):
        (f, s) = (a[i], a[i + 1])
        if f == s:
            print(0)
            return
        if f & x == s & x:
            if count > 2:
                count = 2
        if f == s & x:
            if count > 1:
                count = 1
    if count == 9999:
        print(-1)
    else:
        print(count)


def main():
    (n, x) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    anded = set()
    count = 9999
    a.sort()
    init = {}
    for (i, e) in enumerate(a):
        if e not in init:
            init[e] = set()
        init[e].add(i)
    for i in range(len(a)):
        f = a[i]
        if i < len(a) - 1:
            s = a[i + 1]
            if f == s:
                print(0)
                return
        fx = f & x
        init[f].remove(i)
        if fx in init and init[fx]:
            if count > 1:
                count = 1
        init[f].add(i)
        if fx in anded:
            if count > 2:
                count = 2
        anded.add(fx)
    if count == 9999:
        print(-1)
    else:
        print(count)


def __starting_point():
    main()


__starting_point()
