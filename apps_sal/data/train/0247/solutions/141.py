class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        l = len(arr)
        left, right, pre = [l]*l, [l]*l, {0:-1}
        p = 0
        for i in range(l):
            p += arr[i]
            if p - target in pre:
                prev = pre[p - target]
                left[i] = i - prev
                if prev >= 0:
                    right[prev] = min(right[prev], i - prev)
            pre[p] = i
        
        for i in range(1, l):
            left[i] = min(left[i], left[i-1])
        
        for i in range(l-2, -1, -1):
            right[i] = min(right[i], right[i+1])
        
        ans = l + 1
        
        # for i in range(l):
        #     if left[i] < l and right[i] < l:
        #         ans = min(ans, left[i] + right[i])
        ans = min( left[i] + right[i] if left[i] < l and right[i] < l else l + 1 for i in range(l) )
        
        return ans if ans < l + 1 else -1
        
        

