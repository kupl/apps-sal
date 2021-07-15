class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''
        two passes, extact k times = at most k times - at most k - 1 times
        '''
        def atMost(A: List[int], k: int) -> int:
            i = ret = 0
            for j in range(len(A)):
                if A[j] & 1:
                    k -= 1
                while k < 0:
                    k += A[i] & 1
                    i += 1
                ret += j - i + 1
            return ret 
        
        return atMost(nums, k) - atMost(nums, k-1)
            

