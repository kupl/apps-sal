for tcase in range(int(input())):
    nitems, coins, k = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    ls.sort()
    if ls[0] > coins:
        print(0)
        continue
    best = 0
    spent = 0
    ptr = 0
    while ptr + 1 < nitems and spent + ls[ptr+1] <= coins:
        spent += ls[ptr+1]
        ptr += 2
    if ptr < nitems and spent + ls[ptr] <= coins:
        spent += ls[ptr]
        ptr += 1
    best = ptr

    spent = ls[0]
    ptr = 1
    while ptr + 1 < nitems and spent + ls[ptr+1] <= coins:
        spent += ls[ptr+1]
        ptr += 2
    if ptr < nitems and spent + ls[ptr] <= coins:
        spent += ls[ptr]
        ptr += 1
    best = max(best,ptr)
    print(best)

