class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False
        
        #start = 10**9
        #end = 1
        
        v_cnt = collections.defaultdict(int)
        for v in nums:
            v_cnt[v] += 1
            
        for v in sorted(v_cnt.keys()):
            if v_cnt[v] == 0:
                continue
            else:
                l = v_cnt[v]
                for nv in range(v+1, v+k):
                    if v_cnt[nv] < l:
                        return False
                    v_cnt[nv] -= l
        
        return True
