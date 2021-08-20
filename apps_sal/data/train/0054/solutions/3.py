for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    a.sort(reverse=True)
    t = 2048
    for i in a:
        if t - i >= 0:
            t -= i
    print(['NO', 'YES'][t == 0])
