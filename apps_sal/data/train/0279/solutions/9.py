class Solution:

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ret = ''
        strs = [str(_) for _ in range(1, n + 1)]
        divisor = 1
        for i in range(1, n + 1):
            divisor *= i
        total_index = k - 1
        while len(ret) < n:
            divisor //= len(strs)
            index = total_index // divisor
            total_index %= divisor
            ret += strs[index]
            strs.pop(index)
        return ret
