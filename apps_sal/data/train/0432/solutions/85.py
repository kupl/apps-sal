from collections import defaultdict, OrderedDict
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        
        nums_dict_ordered = OrderedDict(sorted(nums_dict.items()))
        
        while len(nums_dict_ordered) > 0:
            first = next(iter(nums_dict_ordered))
            nums_dict_ordered[first] -= 1
            if nums_dict_ordered[first] == 0:
                    del nums_dict_ordered[first]
            for val in range(1, k):
                check = first+val
                if check not in list(nums_dict_ordered.keys()) or  nums_dict_ordered[check] == 0:
                    return False
                else:
                    nums_dict_ordered[check] -= 1
                if nums_dict_ordered[check] == 0:
                    del nums_dict_ordered[check]
            
        return True

