class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0:
            return -1
        ans = 1
        check = 1
        while check <= K:
            if ans % K == 0:
                return check

            ans = ans * 10 + 1
            check = check + 1
        return -1
