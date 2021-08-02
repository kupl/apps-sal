def getNum():
    inp = input()
    return int(inp)


def getArrNum():
    inp = input()
    A = [int(x) for x in inp.split(' ')]
    return A


def getMaximal(arr):
    best = 0
    curBest = 0
    for x in arr:
        if curBest >= 0:
            curBest += x
        else:
            curBest = x
        best = max(best, curBest)
    return best


def __starting_point():
    N = getNum()
    arr = getArrNum()
    odd = []
    even = []
    for i in range(N - 1):
        nm = abs(arr[i] - arr[i + 1])
        neg = nm * -1
        if i % 2 == 0:
            odd.append(nm)
            even.append(neg)
        else:
            odd.append(neg)
            even.append(nm)
    ans = max(getMaximal(odd), getMaximal(even))
    print(ans)


__starting_point()
