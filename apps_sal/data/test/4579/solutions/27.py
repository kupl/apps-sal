def __starting_point():

    n = int(input())
    ans = set()
    for s in range(n):
        cmd = input()
        ans.add(cmd)
    print((len(ans)))


__starting_point()
