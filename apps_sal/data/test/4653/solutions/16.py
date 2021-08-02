for tc in range(int(input())):
    ncand, nkid = list(map(int, input().split()))
    res = (ncand // nkid) * nkid
    ncand -= res
    res += min(ncand, nkid // 2)
    print(res)
