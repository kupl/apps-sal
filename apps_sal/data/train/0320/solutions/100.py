class Solution:
    def getPow(self, n: int) -> Tuple[int, int]:
        if n == 0:
            return (0, -1)
        if n == 1:
            return (1, 0)
        
        inc = 0
        mul = 0
        i = n
        while i != 0:
            if i % 2 == 1:
                inc += 1
                i = i - 1
            else:
                i = i // 2
                mul += 1
        return (inc, mul)

    def minOperations(self, nums: List[int]) -> int:
        pows = [self.getPow(n) for n in nums]
        
        num_incs = 0
        num_mults = 0
        
        max_pow = 0
        
        for i in range(0, len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] == 1:
                num_incs += 1
            else:
                inc = pows[i][0]
                power = pows[i][1]
                num_incs += inc
                if power > max_pow:
                    max_pow = power
                    
        num_incs += max_pow
        return num_incs
        

