class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left_idx, right_idx = 0, n - 1
        # edge case
        # left side
        while left_idx < n - 1 and arr[left_idx] <= arr[left_idx + 1]:
            left_idx += 1    
        # right side 
        while right_idx > 0 and arr[right_idx - 1] <= arr[right_idx]:
            right_idx -= 1
        nums_to_rm = min(n - left_idx - 1, right_idx)
        
        # print(nums_to_rm)
        
        # general case 
        for curr_idx in range(left_idx + 1):
            if arr[curr_idx] <= arr[right_idx]: 
                nums_to_rm = min(nums_to_rm, max(0, right_idx - curr_idx - 1))
                # print(nums_to_rm)
            else:
                # arr[curr_idx] > arr[right_idx]
                if right_idx < n - 1:
                    right_idx += 1
                else:
                    break
        # [1,2,3,10,4,2,3,5]
        # [5,4,3,2,1]
        # [1]
        return nums_to_rm
