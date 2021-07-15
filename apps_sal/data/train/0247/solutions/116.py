class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # left to right, compute min length of subarray using elems from 0 up to and including i
        # right to left, compute min length of subarray using elems from i+1 to n-1
        # go thru array, pick i s.t. leftmin[i] + rightmin[i] is smallest
        
        n = len(arr)
        
        # compute left to right
        curr_sum = 0
        curr_best = -1
        
        lo = hi = 0
        lmin = []
        while lo <= hi < n:
            curr_sum += arr[hi]
            
            while curr_sum > target and lo <= hi:
                curr_sum -= arr[lo]
                lo += 1
            
            if curr_sum == target:
                tmp = (hi-lo+1)
                if tmp < curr_best or curr_best == -1:
                    curr_best = tmp
            
            lmin.append(curr_best)
            hi += 1
        

        # compute right to left
        curr_sum = 0
        curr_best = -1
        
        lo = hi = n-1
        rmin = [-1] # since lo is exclusive, rmin[n-1] should be -1
        while 0 < lo <= hi:
            curr_sum += arr[lo]
            
            while curr_sum > target and lo <= hi:
                curr_sum -= arr[hi]
                hi -= 1
            
            if curr_sum == target:
                tmp = (hi-lo+1)
                if tmp < curr_best or curr_best == -1:
                    curr_best = tmp
            
            rmin.append(curr_best)
            lo -= 1

        rmin = rmin[::-1]
        
        # print(lmin)
        # print(rmin)
        
        # compute best
        res = -1
        for i in range(n):
            if lmin[i] != -1 and rmin[i] != -1:
                if res == -1 or lmin[i]+rmin[i] < res:
                    res = lmin[i] + rmin[i]
        
        return res
