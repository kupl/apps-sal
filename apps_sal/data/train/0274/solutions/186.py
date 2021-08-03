from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        arr = nums
        lim = limit
        p1 = 0
        p2 = 0
        ans = 1
        bt = SortedList([arr[0]])
        n = len(arr)

        while p1 < n - 1 or p2 < n - 1:

            mx = bt[-1]
            mn = bt[0]
            diff = abs(mx - mn)

            if diff <= lim and ans < p2 - p1 + 1:
                ans = p2 - p1 + 1

            if p2 == n - 1 or diff > lim:
                bt.remove(arr[p1])
                p1 += 1
            else:
                p2 += 1
                bt.add(arr[p2])

        return ans
