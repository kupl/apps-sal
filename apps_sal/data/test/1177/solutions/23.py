import numpy as np

def main():
    n, s = list(map(int, input().split()))
    nums = [int(c) for c in input().split()]
    mod = 998244353
    dp = np.zeros(s+1, dtype=np.int)
    ans = 0

    for i, num in enumerate(nums, 1):
        dp[0] = i
        if num <= s:
            dp[num:] = dp[num:] + dp[:-num]
            # print(dp)
        dp %= mod
        ans = (ans + dp[-1]) % mod
    print(ans)


def __starting_point():
    main()

__starting_point()
