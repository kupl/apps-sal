class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        stack = [[len(arr)-1, arr[-1]]]
        
        for i in range(len(arr)-2, -1, -1):
            if arr[i] <= arr[i+1]:
                stack.append([i, arr[i]])
            else:
                break
        
        min_len = len(arr)-len(stack)
        
        for i in range(len(arr)):
            if i == 0 or arr[i] >= arr[i-1]:
                while len(stack) > 0 and (stack[-1][1] < arr[i] or stack[-1][0] <= i):
                    stack.pop()

                if len(stack) > 0:
                    min_len = min(min_len, stack[-1][0]-i-1)
                else:
                    min_len = min(min_len, len(arr)-i-1)
            else:
                break
        
        return min_len
