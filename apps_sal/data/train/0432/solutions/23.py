class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums_counter = collections.Counter(nums)

        while(nums_counter):
            min_ele = min(nums_counter)
            for i in range(k):
                if nums_counter[min_ele+i]:
                    nums_counter[min_ele+i] -= 1
                else:
                    return False
                
                if nums_counter[min_ele+i] == 0:
                    del nums_counter[min_ele+i]
        return True
