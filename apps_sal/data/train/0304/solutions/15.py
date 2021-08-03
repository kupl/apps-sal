class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def counting_sort():
            nonlocal ages
            counts = 120 * [0]
            for i in range(len(ages)):
                counts[ages[i] - 1] += 1
            ages = []
            for i in range(len(counts)):
                ages += [i + 1] * counts[i]
        counting_sort()
        res = 0
        prev = None
        for i in range(len(ages) - 1, -1, -1):
            if i == len(ages) - 1 or ages[i] != ages[i + 1]:
                prev = i
            low, right = 0, prev - 1
            while low < right:
                mid = (low + right) // 2
                if ages[mid] <= 0.5 * ages[prev] + 7:
                    low = mid + 1
                else:
                    right = mid
            if ages[low] > 0.5 * ages[prev] + 7:
                res += (prev - low)
        return res
