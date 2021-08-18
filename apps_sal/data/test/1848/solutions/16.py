def __starting_point():
    n = int(input())
    lst = list(map(int, input().split(' ')))
    lst.sort()
    h, i = 0, 0
    trav = []
    while i < n - 1:
        if i in trav:
            i += 1
            continue
        j = i + 1
        s = lst[i]
        while j < n:
            if lst[j] > s and j not in trav:
                h += 1
                s = lst[j]
                trav.append(j)
            j += 1
        trav.append(i)
        i += 1
    print(h)


__starting_point()
