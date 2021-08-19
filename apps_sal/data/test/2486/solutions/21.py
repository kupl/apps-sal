def main():
    import numpy as np
    from bisect import bisect_left as bl
    mod = 10 ** 9 + 7
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = np.zeros(k, dtype=np.int32)
    dp[0] = 1
    m = bl(a, k)
    for i in range(m):
        aa = a[i]
        dp[aa:] = (dp[aa:] + dp[:k - aa]) % mod

    def b_search(ok, ng):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if value(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def value(i):
        if i == -1:
            return True
        if i == m:
            return False
        aa = a[i]
        dp2 = np.zeros(k, dtype=np.int32)
        dp2[:aa] = dp[:aa]
        for j in range(aa, k):
            dp2[j] = (dp[j] - dp2[j - aa]) % mod
        for j in range(k - aa, k):
            if dp2[j] != 0:
                return False
        return True
    print(b_search(-1, m) + 1)


main()
