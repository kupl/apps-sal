def ApplePie():
    (N, L) = input().split()
    N = int(N)
    L = int(L)
    flavors = []
    for i in range(N):
        flavors.append(L + i)
    if 0 in flavors:
        flavors.remove(0)
        result = 0
        for i in flavors:
            result = result + i
        print(result)
        return
    elif L >= 0:
        del flavors[0]
        result = 0
        for i in flavors:
            result = result + i
        print(result)
        return
    else:
        del flavors[-1]
        result = 0
        for i in flavors:
            result = result + i
        print(result)
        return


ApplePie()
