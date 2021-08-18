class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        trip_zeros = []
        for num in nums:
            if num:
                if trip_zeros:
                    trip_zeros[-1].append(num)
                else:
                    trip_zeros.append([num])
            else:
                trip_zeros.append([])

        def count(arr):
            start = ans = 0
            left_neg = None
            pos = 1
            for end in range(len(arr)):
                if arr[end] < 0:
                    if left_neg is None:
                        left_neg = end
                    pos ^= 1
                print(pos, start, end, left_neg)
                if pos:
                    ans = max(ans, end - start + 1)

                else:
                    ans = max(ans, end - left_neg)
            return ans

        return max(map(count, trip_zeros))
