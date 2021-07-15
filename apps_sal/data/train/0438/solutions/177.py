class Solution:
    def findLatestStep(self, a: List[int], m: int) -> int:
        index2len, len_cnt, last_index = defaultdict(int), Counter(), -1        
        for i, p in enumerate(a):    
            left_len, right_len = index2len[p-1], index2len[p+1]
            new_len = left_len + 1 + right_len
            index2len[p-left_len] = index2len[p+right_len] = new_len
            len_cnt[left_len] -= 1
            len_cnt[right_len] -= 1                
            len_cnt[new_len] += 1 
            if len_cnt[m] > 0: last_index = i + 1            
        return last_index
