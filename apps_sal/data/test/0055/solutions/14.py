

def __starting_point():
    h, k = [int(n) for n in input().split(' ')]
    level = 0
    ret = []
    while h > 0:
        if h % 2 == 0:
            h //= 2
            level += 1
        else:
            ret.append(level)
            h -= 1
    if len(ret) > k:
        print('No')
    else:
        print('Yes')
        cntnum = {}
        maxn = ret[0]
        minn = ret[0]
        total_len = len(ret)
        for i in ret:
            if i not in cntnum:
                cntnum[str(i)] = 0
            cntnum[str(i)] += 1
            if maxn < i:
                maxn = i
            if minn > i:
                minn = i

        while total_len <= k:
            if total_len + cntnum[str(maxn)] <= k:
                if str(maxn - 1) not in cntnum:
                    cntnum[str(maxn - 1)] = 0
                cntnum[str(maxn - 1)] += 2 * cntnum[str(maxn)]
                total_len += cntnum[str(maxn)]
                cntnum[str(maxn)] = 0
                maxn -= 1
                minn = min(minn, maxn)
            else:
                break

        while total_len < k:
            cntnum[str(minn - 1)] = 2
            cntnum[str(minn)] -= 1
            minn -= 1
            total_len += 1

        ans = []
        for num, v in list(cntnum.items()):
            for i in range(0, v):
                ans.append(int(num))
        ans.sort(reverse=True)

        print(" ".join([str(x) for x in ans]))


__starting_point()
