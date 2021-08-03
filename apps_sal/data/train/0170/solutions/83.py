class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # sliding window
        # find the first element which is smaller than the previous one
        start_f = 0
        while start_f < len(arr) - 1:
            if arr[start_f + 1] >= arr[start_f]:
                start_f += 1
            else:
                break

        # if already sorted, end_f is the last element
        if start_f == len(arr) - 1:
            return 0

        # find the end point that let end+1 element > start_f element
        end_f = len(arr) - 1

        if arr[-1] < arr[start_f]:
            end_f = len(arr)
        else:
            while end_f - 1 >= 0 and arr[end_f - 1] >= arr[start_f]:
                if arr[end_f - 1] <= arr[end_f]:  # 逐渐在变小
                    end_f -= 1
                else:  # not sorted， 前面一个数比较大了，那么在往前退，会导致第二部分不是sort的
                    break

        # start,end 是需要remove的
        start, end = start_f + 1, end_f - 1

        ans = end - start + 1

        # 逐渐把start往前1，看能不能得到更小的值
        while start >= 0:
            start -= 1
            while start == 0 or arr[end] >= arr[start - 1]:  # start ==0的时候就没有第一部分了

                if end == len(arr) - 1 or arr[end] <= arr[end + 1]:  # end最大时，就没有第二部分了
                    end -= 1
                    ans = min(ans, end - start + 1)
                else:
                    break
        return ans
