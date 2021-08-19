def main():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]
    YesFlag = True
    arr = [True] * (2 * n + 1)
    cnt = 0
    for (a, b) in AB:
        if a != -1 and b != -1 and (a > b):
            YesFlag = False
        if a != -1 and (not arr[a]):
            YesFlag = False
        if b != -1 and (not arr[b]):
            YesFlag = False
        if a != -1:
            arr[a] = False
        if b != -1:
            arr[b] = False
        if a == -1 and b == -1:
            cnt += 1
    dp = [-1] * (2 * n + 1)
    dp[0] = cnt
    for i in range(0, 2 * n + 1, 2):
        if dp[i] < 0:
            continue
        for j in range(i + 2, 2 * n + 1, 2):
            fs = [True] * (2 * n + 1)
            lngth = (j - i) // 2
            sf = True
            for (a, b) in AB:
                if a == -1 and b == -1 or (a != -1 and (a <= i or j < a)) or (b != -1 and (b <= i or j < b)):
                    continue
                if a != -1 and b != -1:
                    if b - a != lngth or a <= i or j < b:
                        sf = False
                        break
                    elif not fs[a] or not fs[b]:
                        sf = False
                        break
                    else:
                        fs[a] = False
                        fs[b] = False
                elif a == -1:
                    p = b - lngth
                    if p <= i or j < b:
                        sf = False
                        break
                    if not fs[p] or not fs[b]:
                        sf = False
                        break
                    else:
                        fs[p] = False
                        fs[b] = False
                else:
                    q = a + lngth
                    if a <= i or j < q:
                        sf = False
                        break
                    if not fs[a] or not fs[q]:
                        sf = False
                        break
                    else:
                        fs[a] = False
                        fs[q] = False
            if sf:
                c = 0
                for k in range(i + 1, j + 1):
                    if fs[k]:
                        c += 1
                if dp[j] < dp[i] - c // 2:
                    dp[j] = dp[i] - c // 2
    if dp[-1] != 0:
        YesFlag = False
    if YesFlag:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
