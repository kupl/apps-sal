class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
       
        
        # sum_of_mutate(arr, sorted_arr[i]) will be like
        # L L L L M M
        # where L = sum_of_mutate[i] less than or equal target, M = more
        # we want to find last L
        # then answer can be last L or next M whatever make mutate sum smaller
        
        l = 0
        r= max(arr)
        
        while l < r:
            mid = ((l+r) // 2 ) + 1

            if self.sum_of_mutate(arr, mid) > target:
                r = mid - 1
            else:
                l = mid
        if abs(self.sum_of_mutate(arr, l) - target) <=  abs(self.sum_of_mutate(arr, l+1) - target):
            return l
        else:
            return l + 1


    def sum_of_mutate(self, arr, k):
        return sum(min(e, k) for e in arr)
        
        

