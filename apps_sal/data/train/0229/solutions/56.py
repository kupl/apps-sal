class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        pos_set = set()
        neg_set = set()
        pos_dict = {}
        neg_dict = {}
        pos_count = 0
        for num in A:
            if num >= 0:
                pos_set.add(num)
                pos_dict[num] = 1 + pos_dict.get(num,0)
                pos_count += 1
            else:
                neg_set.add(abs(num))
                neg_dict[abs(num)] = 1 + neg_dict.get(abs(num),0)
        if pos_count % 2 != 0:
            return False
        else:
            return self.helper(pos_set,pos_dict) and self.helper(neg_set,neg_dict)
    
    def helper(self,set_,dict_):
        sorted_ = sorted(list(set_))
        for num in sorted_:
            if num * 2 in sorted_ and num != 0:
                small_ = dict_[num] 
                large_ = dict_[num * 2]
                usage = min(small_,large_)
                dict_[num] -= usage
                dict_[num * 2] -= usage
            elif num == 0:
                if dict_[0] % 2 != 0:
                    return False
                else:
                    dict_[0] = 0
                
        for key in dict_:
            if dict_[key] != 0:
                return False
        return True
                

