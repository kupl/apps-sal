class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remainder = 1
        curr_len = 1
        for i in range(K + 1):
            if remainder % K == 0:
                return curr_len
            else:
                remainder = (remainder * 10 + 1) % K
                curr_len += 1
        return -1
