def run():
    (n, a, b) = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]
    main = d[0]
    other = d[1:]
    other.sort()
    ans = n - 1
    s = main
    for x in other:
        if main * a < b * (s + x):
            print(ans)
            return
        s += x
        ans -= 1
    print(0)


run()
