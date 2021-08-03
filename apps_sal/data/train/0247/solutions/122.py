class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        # m[i]: min length and and in i, included

        ptr1, ptr2 = 0, 0  # both inclusive
        s = arr[0]  # cum sum
        m = [-1] * len(arr)
        ans = -1
        global_min = -1

        while ptr2 < len(arr):
            if global_min > 0:
                m[ptr2] = global_min
            if s == target:
                m[ptr2] = min(global_min, ptr2 - ptr1 + 1) if global_min > 0 else ptr2 - ptr1 + 1
                global_min = m[ptr2]
                if ptr1 - 1 >= 0 and m[ptr1 - 1] > 0:
                    ans = min(ans, m[ptr1 - 1] + ptr2 - ptr1 + 1) if ans > 0 else m[ptr1 - 1] + ptr2 - ptr1 + 1
                ptr1 += 1
                ptr2 += 1
                if ptr2 < len(arr):
                    s = s - arr[ptr1 - 1] + arr[ptr2]
            elif s > target:
                ptr1 += 1
                s = s - arr[ptr1 - 1]
                if ptr1 > ptr2 and ptr2 + 1 < len(arr):
                    ptr2 += 1
                    s = s + arr[ptr2]
            else:
                ptr2 += 1
                if ptr2 < len(arr):
                    s = s + arr[ptr2]

        return ans
