class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        start_mp, end_mp = {}, {}
        max_step = -1
        m_cnt = 0
        for idx, num in enumerate(arr): 
            l = 1
            if num-1 not in end_mp and num+1 not in start_mp: 
                start_mp[num] = end_mp[num] = 1
                start_index = end_index = num
            elif num-1 in end_mp and num +1 in start_mp:
                # merge
                old_l = end_mp[num-1]
                old_r = start_mp[num+1]
                if old_l == m: 
                    m_cnt -= 1
                if old_r == m: 
                    m_cnt -= 1
                start_index = num-1 - end_mp[num-1] + 1
                end_index = num+1 + start_mp[num+1] -1
                l = end_mp[num-1] + start_mp[num+1] + 1
                del end_mp[num-1], start_mp[num-1-old_l+1], start_mp[num+1], end_mp[num+1+old_r-1]
                start_mp[start_index] = l
                end_mp[end_index] = l
            elif num-1 in end_mp: 
                # extend to the left
                old_l = end_mp[num-1]
                if old_l == m: 
                    m_cnt -= 1
                l = old_l + 1
                del end_mp[num-1], start_mp[num-1-old_l+1]
                start_index = num-l+1 
                end_index = m
                end_mp[num] = start_mp[num-l+1] = l
            elif num+1 in start_mp: 
                old_l = start_mp[num+1]
                if old_l == m: 
                    m_cnt -= 1
                l = old_l + 1
                del end_mp[num+1+old_l-1], start_mp[num+1]
                start_mp[num] = end_mp[num+l-1] = l
                start_index = num
                end_index = num+l-1
            
            if l == m: 
                m_cnt += 1
            if m_cnt > 0: 
                max_step = max(max_step, idx + 1)
        return max_step
                
                
            
            
            
                
            
            
            
            
            

