
def main():
    n, k = list(map(int, input().split()))
    myList = list(map(int, input().split()))
    i = 0
    distinct = 0
    dictOf = [0] * 1000001
    best = 0
    bestX = 0
    bestY = 0
    for j in range(n):
        dictOf[myList[j]] += 1
        if dictOf[myList[j]] == 1:
            distinct += 1
        while distinct > k:
            dictOf[myList[i]] -= 1
            if dictOf[myList[i]] == 0:
                distinct -= 1
            i += 1
        if j - i + 1 > best:
            best = j - i + 1
            bestX = i + 1
            bestY = j + 1
    print(bestX, bestY)


def __starting_point():
    main()


__starting_point()
