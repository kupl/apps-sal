def solve(n, k):
    dp = [420] * (len(k) + 1)
    dp[-1] = 0
    idx = len(k) - 1
    n_num = int(n)
    while idx >= 0:
        if k[idx] != '0':
            for shift in range(1, len(k) - idx + 1):
                ok = int(k[idx:idx + shift]) < n_num
                if ok:
                    dp[idx] = min(
                        dp[idx], 1 + dp[idx + shift]
                    )
                else:
                    break
        else:
            dp[idx] = 1 + dp[idx + 1]
        idx -= 1
    digits = list()
    idx = 0
    while idx < len(k):
        shift = 1
        while idx + shift <= len(k):
            if dp[idx + shift] + 1 == dp[idx]:
                digits.append(int(k[idx:idx + shift]))
                break
            else:
                shift += 1
        idx += shift
    tot_res, n_pow = 0, 1
    for el in reversed(digits):
        tot_res += n_pow * el
        n_pow *= n_num
    return tot_res


N = input()
K = input()
print(solve(N, K))
