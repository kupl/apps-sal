class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        m = Counter()
        cur_sum = 0
        ans = 0
        for x in A:
            cur_sum += x
            ans += m[cur_sum % K]
            if cur_sum % K == 0:
                ans += 1
            print((x, m[cur_sum % K]))
            m[cur_sum % K] += 1
        return ans
