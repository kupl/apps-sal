class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        s2 = []
        for i in nums:
            n1 = 0
            m = 0
            for j in range(32):
                if i & (2**j) != 0:
                    m = j
                    n1 += 1
            ans += n1
            s2.append(m)
        s2.sort()

        ans += s2[0]

        for i in range(1, len(s2)):
            ans += s2[i] - s2[i - 1]
        return ans
