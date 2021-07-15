class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if len(nums) % k != 0:
            return False
        count = dict(Counter(nums))
        nums = sorted(list(set(nums)))
        for num in nums:
            if count[num] != 0:
                for i in range(1, k):
                    if num + i not in count:
                        return False
                    else:
                        count[num+i] -= count[num]
            count[num] = 0
           # print(count)
        return all([a == 0 for a in list(count.values())])

