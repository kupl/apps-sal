class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if not K%2:
            return -1
        ans = 1
        count = 1
        while count<=K:
            if ans%K == 0:
                return count
            ans = ans*10 + 1
            count += 1
        
        return -1

