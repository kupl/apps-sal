def __starting_point():
    S = input()
    x = ['A', 'C', 'G', 'T']
    ans = 0
    now = 0
    for s in S:
        if s in x:
            now += 1
        else:
            now = 0
        ans = max(now, ans)
    print(ans)
__starting_point()
