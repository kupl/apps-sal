class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        dic = collections.Counter()
        dic[0] += 1
        pre = ans = 0
        for (i, x) in enumerate(arr):
            pre += x
            pre %= 2
            ans = (ans + dic[pre ^ 1]) % mod
            dic[pre] += 1
        return ans
