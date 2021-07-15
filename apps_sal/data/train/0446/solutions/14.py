import collections
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        
        value_counter = collections.Counter(list(counter.values()))
        remaining = len(counter)
        
        for val_count_key in range(1, len(arr) + 1):
            if k >= val_count_key * value_counter[val_count_key]:
                k -= val_count_key * value_counter[val_count_key]
                remaining -= value_counter[val_count_key]
            else:
                return remaining - k//val_count_key
            
        return remaining
        
        
        

