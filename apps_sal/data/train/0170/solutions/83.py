class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        start_f = 0
        while start_f < len(arr) - 1:
            if arr[start_f + 1] >= arr[start_f]:
                start_f += 1
            else:
                break

        if start_f == len(arr) - 1:
            return 0

        end_f = len(arr) - 1

        if arr[-1] < arr[start_f]:
            end_f = len(arr)
        else:
            while end_f - 1 >= 0 and arr[end_f - 1] >= arr[start_f]:
                if arr[end_f - 1] <= arr[end_f]:
                    end_f -= 1
                else:
                    break

        start, end = start_f + 1, end_f - 1

        ans = end - start + 1

        while start >= 0:
            start -= 1
            while start == 0 or arr[end] >= arr[start - 1]:

                if end == len(arr) - 1 or arr[end] <= arr[end + 1]:
                    end -= 1
                    ans = min(ans, end - start + 1)
                else:
                    break
        return ans
