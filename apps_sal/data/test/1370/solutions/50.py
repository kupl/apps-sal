def column_check(grp, grp_count, choco, h, j, k):
    """ 0:成功（更新も反映）  1:失敗（区切った結果を返す） 2:不可能 """
    curr_count = [0] * len(grp_count)
    for i in range(h):
        if choco[i][j] == '0':
            continue
        curr_count[grp[i]] += 1
    for cc in curr_count:
        if cc > k:
            return 2
    for (i, cc) in enumerate(curr_count):
        grp_count[i] += cc
        if grp_count[i] > k:
            grp_count[:] = curr_count
            return 1
    return 0


def solve(h, w, k, choco):
    ans = 10 ** 9
    grp = [0] * h
    for bit in range(1 << h - 1):
        g = 0
        for i in range(h):
            grp[i] = g
            if bit >> i & 1:
                g += 1
        grp_count = [0] * (g + 1)
        tmp = 0
        possible = True
        for j in range(w):
            result = column_check(grp, grp_count, choco, h, j, k)
            if result == 2:
                possible = False
                break
            if result == 1:
                tmp += 1
        if not possible:
            continue
        ans = min(ans, tmp + bin(bit).count('1'))
    return ans


(h, w, k) = list(map(int, input().split()))
choco = [input() for _ in range(h)]
print(solve(h, w, k, choco))
