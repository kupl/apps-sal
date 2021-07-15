class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr = [0] + arr + [float('inf')]
        left = 0
        right = len(arr) - 1
        
        while left != right:
            if arr[left + 1] < arr[left]:
                break
            left += 1
            
        while left != right:
            if arr[right - 1] > arr[right]:
                break
            right -= 1
            
        if right == left: return 0
        
        return search(left, right, arr)
        

def search(leftidx, rightidx, arr):
    if arr[rightidx] >= arr[leftidx]: return rightidx - leftidx - 1
    leftsearch = rightsearch = midsearch = len(arr)
    if leftidx > 0:
        leftsearch = search(leftidx - 1, rightidx, arr)
    if rightidx < len(arr) - 1:
        rightsearch = search(leftidx, rightidx + 1, arr)
    if leftidx > 0 and rightidx < len(arr) - 1:
        midsearch = search(leftidx - 1, rightidx + 1, arr)
    
    return min(leftsearch, rightsearch, midsearch)
