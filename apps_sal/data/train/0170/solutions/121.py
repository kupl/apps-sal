class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        first, last = -1, -1
        length = len(arr)
        prev = float('-inf')
        for i in range(length):
            if arr[i] < prev:
                first = i
                break
            prev = arr[i]
        if first == -1:
            return 0
        after = float('inf')
        for i in range(length - 1, -1, -1):
            if arr[i] > after:
                last = i
                break
            after = arr[i]
            
        def helper(size):
            for i in range(length - size + 1):
                if i <= first and i + size > last:
                    if i + size == length or i == 0:
                        return True
                    if arr[i + size] >= arr[i - 1]:
                        return True
            return False
            
        low, high = 1, length - 1
        res = float('inf')
        while low <= high:
            mid = low + (high - low) // 2
            if helper(mid):
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res
