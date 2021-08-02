def __starting_point():
    inp = input()
    arr = input().split(' ')
    cz = 0
    cf = 0
    for a in arr:
        if int(a) == 0:
            cz += 1
        if int(a) == 5:
            cf += 1
    ans = '-1'
# print(cf)
# print(cz)
    if cz == 0:
        ans = '-1'
    else:
        ng = cf // 9
        ans = '555555555' * ng + '0' * cz
    print(int(ans))


__starting_point()
