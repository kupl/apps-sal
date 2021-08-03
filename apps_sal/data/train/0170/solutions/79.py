class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        desc_idx = []
        for idx in range(len(arr)):
            if idx > 0 and arr[idx] < arr[idx - 1]:
                desc_idx.append(idx - 1)

        if len(desc_idx) == 0:
            return 0
        ans = len(arr)
        start, end = desc_idx[0], desc_idx[-1]
        shift_range = [0, 1]
        for shift1 in shift_range:
            for shift2 in shift_range:
                left = arr[:start + shift1]
                right = arr[end + 1 + shift2:]
                left_extend = -1
                right_extend = -1

                if len(left) == 0:
                    right_extend = 0
                else:
                    for idx in range(len(right)):
                        if right[idx] >= left[-1]:
                            right_extend = idx
                            break
                    if right_extend == -1:
                        right_extend = len(right)

                if len(right) == 0:
                    left_extend = 0
                else:
                    for idx in range(len(left)):
                        if left[-(idx + 1)] <= right[0]:
                            left_extend = idx
                            break
                    if left_extend == -1:
                        left_extend = len(left)

                ans = min(ans, min(left_extend, right_extend) + (end + 1 + shift2) - (start + shift1))
                # extend.append(left_extend)
                # extend.append(right_extend)

        #print(extend, ans, desc_idx)
        #ans += min(extend)
        return ans
