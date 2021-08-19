class Solution:

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        m = min(arr)
        M = max(arr)
        s = sum(arr)
        if m > 0:
            return s * k
        if M < 0:
            return 0
        ans = 0
        prefix_sum = 0
        m_prefix_sum = 0
        for num in arr:
            prefix_sum += num
            ans = max(ans, prefix_sum - m_prefix_sum)
            m_prefix_sum = min(m_prefix_sum, prefix_sum)
        if k == 1:
            return ans
        prefix_sum = 0
        p_M = 0
        for num in arr:
            prefix_sum += num
            p_M = max(p_M, prefix_sum)
        suffix_sum = 0
        s_M = 0
        for num in arr[::-1]:
            suffix_sum += num
            s_M = max(s_M, suffix_sum)
        return max(ans, p_M + s_M + (k - 2) * s, p_M + s_M) % (10 ** 9 + 7)
