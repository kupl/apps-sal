# 829
class Solution:
    def maxDistance(self, arr: List[int], m: int) -> int:
        arr.sort()
        low = 1
        high = arr[-1] - arr[0]

        def place(limit):
            prev = -1e10
            j = 0
            for i in range(m):
                while j < len(arr) and arr[j] - prev < limit:
                    j += 1
                if j == len(arr):
                    return False
                prev = arr[j]
                j += 1

            return True

        while low <= high:
            cur = int((low + high) / 2)
            #print(low, high, cur, place(cur))
            if place(cur):
                low = cur + 1
            else:
                high = cur - 1
        return high
