
def main():
    n, k = list(map(int, input().split()))
    cowLocations = input()
    whereIsCow = []
    for i in range(len(cowLocations)):
        if cowLocations[i] == '0':
            whereIsCow.append(i)
    i = 0
    j = k
    fJohn = 0
    wic = len(whereIsCow)
    smallest = 1000000
    while i < wic and j < wic and fJohn < wic:
        maxDist = max(whereIsCow[j] - whereIsCow[fJohn],
                      whereIsCow[fJohn] - whereIsCow[i])
        while fJohn <= j and max(whereIsCow[j] - whereIsCow[fJohn + 1],
                                 whereIsCow[fJohn + 1] - whereIsCow[i]) < maxDist:
            fJohn += 1
            maxDist = max(whereIsCow[j] - whereIsCow[fJohn],
                          whereIsCow[fJohn] - whereIsCow[i])
        if maxDist < smallest:
            smallest = maxDist
        j += 1
        i += 1
    print(smallest)


def __starting_point():
    main()


__starting_point()
