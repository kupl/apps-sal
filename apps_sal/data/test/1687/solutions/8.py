def f():
    input()
    a = list(map(int, input().split(' ')))
    m = min(a)
    for i in a:
        if i % m != 0:
            print(-1)
            break
    else:
        print(m)


f()
