def __starting_point():
    n = int(input())
    aa = list(map(int, input().split()))
    (odd, even) = (False, False)
    for a in aa:
        if a % 2 == 0:
            odd = True
        else:
            even = True
        if odd and even:
            break
    if odd and even:
        aa.sort()
    print(' '.join(map(str, aa)))


__starting_point()
