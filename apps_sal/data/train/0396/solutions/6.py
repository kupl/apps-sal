class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2==0 or K%5==0:
            return -1
        n = 0
        seen = set()
        for i in range(K):
            n = (n*10+1)%K
            if n==0:
                return i+1
            elif n in seen:
                return -1
            seen.add(n)
        return -1
