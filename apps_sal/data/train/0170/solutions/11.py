class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # check best from left
        # check best from right
        left, right = 0, len(arr) - 1
        while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == len(arr) - 1:
            return 0
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        best = min(len(arr) - 1 - left, right)  # only prefix or suffix parts

        # merging prefix and suffix
        # first checking all elements smaller than left to see which ones can be used before the right index draw a line going from (0,0) -> (3,2) and a line going form (7, 1) -> (10, 3) and notice which arrays you can make by drawing horizontal lines on y = 1 and y = 2.
        # Essentially we start from the beginning and we see which ones from the left can exist if right is where it was before. If we get to a left that is greater than right, we increment right by 1 to see if the next left < the next right. We keep on repeating this process until we cant (when the current left is greater than the current right and the current right is the last element). At that point, we just return the smallest we have seen until that time.
        for i in range(left + 1):
            if arr[i] <= arr[right]:
                best = min(best, right - i - 1)
            elif right < len(arr) - 1:
                right += 1
            else:
                break
        # The following method fails for [1,2,3,10,0,7,8,9]
        # for i in range(left + 1):
        #     if arr[i] <= arr[right]:
        #         best = min(best, right - i - 1)
        # for i in range(len(arr) - 1, right - 1, -1):
        #     print(arr[left], arr[i])
        #     if arr[left] <= arr[i]:
        #         best = min(best, i - left - 1)
        return best
