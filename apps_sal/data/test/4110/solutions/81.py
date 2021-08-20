def main():
    (D, G) = map(int, input().split())
    ListPC = [list(map(int, input().split())) for d in range(D)]
    ans = sum([i[0] for i in ListPC])
    for i in range(2 ** D):
        (TempPoint, num, restmax) = (0, 0, -1)
        for j in range(D):
            if i >> j & 1:
                TempPoint += 100 * (j + 1) * ListPC[j][0] + ListPC[j][1]
                num += ListPC[j][0]
            else:
                restmax = max(j, restmax)
        if TempPoint >= G:
            ans = min(num, ans)
        elif (G - TempPoint) // ((restmax + 1) * 100) <= ListPC[restmax][0]:
            ans = min(num + (G - TempPoint - 1) // ((restmax + 1) * 100) + 1, ans)
    print(ans)


def __starting_point():
    main()


__starting_point()
