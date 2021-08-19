def hoge():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    sys.setrecursionlimit(max(1000, 10**9))

    from collections import defaultdict
    n = int(input())
    ns = defaultdict(set)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        ns[u - 1].add(v - 1)
        ns[v - 1].add(u - 1)

    M = 10**9 + 7  # 出力の制限
    N = n  # 必要なテーブルサイズ

    g1 = [None] * (N + 1)  # 元テーブル
    g2 = [None] * (N + 1)  # 逆元テーブル
    inverse = [None] * (N + 1)  # 逆元テーブル計算用テーブル
    g1[0] = g1[1] = g2[0] = g2[1] = 1
    inverse[0], inverse[1] = [0, 1]

    for i in range(2, N + 1):
        g1[i] = (g1[i - 1] * i) % M
        inverse[i] = (-inverse[M % i] * (M // i)) % M  # ai+b==0 mod M <=> i==-b*a^(-1) <=> i^(-1)==-b^(-1)*aより
        g2[i] = (g2[i - 1] * inverse[i]) % M

    ans = {}
    prevs = {}
    out = [None] * n

    def sub(i, j, prev):
        prevs[i, j] = prev
        if (i, j) in ans:
            return ans[i, j]
        if len(ns[j]) == 1 and i in ns[j]:
            ans[i, j] = (1, 1)
            return (1, 1)

        count = 1
        sum_size = 0
        for k in ns[j]:
            if k == i:
                continue
            val, size = sub(j, k, i)
            count = (count * val) % M
            count = (count * g2[size]) % M
            sum_size += size
        count = (count * g1[sum_size]) % M
        ans[i, j] = (count, sum_size + 1)
        return (count, sum_size + 1)

    def sub2(i, j):
        for k in ns[j]:
            if k == i:
                continue
            if (k, j) in ans:
                continue
            tmp_count, tmp_size = ans[j, k]
            total_count, total_size = ans[prevs[j, k], j]
            prev_count, prev_size = ans[j, i]
            new_size = total_size - tmp_size + prev_size
            new_count = (total_count * g2[total_size - 1] * g1[new_size - 1]) % M
            new_count = (new_count * prev_count * pow(tmp_count, M - 2, M)) % M
            new_count = (new_count * g2[prev_size] * g1[tmp_size]) % M
            ans[k, j] = (new_count, new_size)
            val = tmp_count
            val = (val * new_count * g1[new_size + tmp_size - 1] * g2[tmp_size - 1] * g2[new_size]) % M
            out[k] = val
            sub2(j, k)
    #         print("total: ", total_count, total_size)
    #         print("tmp: ", tmp_count, tmp_size)
    #         print("prev: ", prev_count, prev_size)
    #         new_count = total_count / g1[total_size-1] * g1[new_size-1] * prev_count / tmp_count / g1[prev_size] * g1[tmp_size]
    #         print(new_count)
    #         print("")

    # 0を始点として木DP
    sub(-1, 0, None)

    ans[0, -1] = (1, 0)

    # 逆向きを求める
    sub2(-1, 0)

    u = 0
    count = 1
    sum_size = 0
    for k in ns[u]:
        val, size = ans[u, k]  # sub(u, k, None)
        count = (count * val) % M
        count = (count * g2[size]) % M
        sum_size += size
    count = (count * g1[sum_size]) % M
    out[0] = count
    print("\n".join(map(str, out)))


hoge()
