import numpy as np

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        a = np.array(sorted(A))
        non_pos_idxs = np.where(a >= 0)[0]
        if len(non_pos_idxs) > 0:
            non_pos_idx = non_pos_idxs[0]
        else:
            non_pos_idx = len(a)
        b = a[:non_pos_idx][::-1]
        a = a[non_pos_idx:]
        if len(b) % 2 != 0:
            return False
        
        if not self.check_doubled(a):
            return False
        if not self.check_doubled(b):
            return False
        return True
    
    def check_doubled(self, a):
        if len(a) == 0:
            return True
        count_dict = {}
        for val in a:
            if count_dict.get(val, 0) > 0:
                count_dict[val] -= 1
            else:
                count_dict[2 * val] = count_dict.get(2 * val, 0) + 1
        for val in list(count_dict.values()):
            if val > 0:
                return False
        return True

