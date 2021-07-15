class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        if (N % k != 0):
            return False
        
        counter = collections.Counter(nums)
        while (counter):
            min_key = min(counter.keys())
            for i in range(k):
                if (min_key in counter):
                    counter[min_key] -= 1
                    if (counter[min_key] == 0):
                        del counter[min_key]
                    min_key += 1
                else:
                    return False
        
        return True
