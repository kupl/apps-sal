def main():
    import numpy as np
    (n, k) = list(map(int, input().split()))
    H = list(map(int, input().split()))
    s = np.array(sorted(set(H + [0])), dtype=np.int64)
    d = {i: j for (j, i) in enumerate(s)}
    l = len(s)
    dp = np.full((k + 1, l), 10 ** 13, dtype=np.int64)
    dp2 = np.zeros((k + 1, l), dtype=np.int64)
    dp[0, 0] = 0
    for h in H:
        dh = d[h]
        dp2 = np.zeros((k + 1, l), dtype=np.int64)
        dp2[0] = np.full(l, 10 ** 13, dtype=np.int64)
        dp2[1:, :] = dp[:-1, :]
        temp = np.min(dp + np.concatenate([(h - s)[:dh], np.zeros(l - dh, dtype=np.int64)]), axis=1)
        dp2[:, dh] = np.minimum(dp2[:, dh], temp[:])
        dp = dp2
    print(np.min(dp))


main()
