def main():
    n, k = map(int, input().split())
    inlis = list(map(int, input().split()))
    indic = dict()
    cnt = 0
    for i in range(n):
        num = inlis[i]
        if num in indic:
            indic[num] += 1
        else:
            indic[num] = 1
            cnt += 1
    if cnt <= k:
        print(0)
    else:
        indic_sort = sorted(indic.items(), key=lambda x: x[1])
        sa = cnt - k
        tmp = 0
        ans = 0
        for j in range(n):
            tmp += 1
            ans += indic_sort[j][1]
            if tmp == sa:
                break
        print(ans)


def __starting_point():
    main()


__starting_point()
