def dlen(n):
    ans = 0
    while n > 0:
        ans += 1
        n //= 10
    return ans


def backtrack(i, s, k, memo):
    n = len(s)
    if k < 0:
        return float('inf')
    elif i == n or k >= n - i:
        return 0
    elif (i, k) in memo:
        return memo[i, k]
    else:
        ans = float('inf')
        count = defaultdict(int)
        most_freq = 0
        for start in range(i, n):
            char = s[start]
            count[char] += 1
            most_freq = max(most_freq, count[char])
            digit_len = 0 if most_freq == 1 else len(str(most_freq))
            ans = min(ans, 1 + digit_len + backtrack(start + 1, s, k - (start - i + 1 - most_freq), memo))
        memo[i, k] = ans
        return ans


class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        memo = {}
        return backtrack(0, s, k, memo)
