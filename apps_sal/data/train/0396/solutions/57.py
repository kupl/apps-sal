class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K %2 == 0:
            return -1
        factor = 1
        length = 1
        remainder = set()
        while(True):
            if factor % K == 0:
                return length
            rem = factor%K
            if rem not in remainder:
                remainder.add(rem)
            else:
                return -1
            factor = factor*10 + 1
            length+= 1

