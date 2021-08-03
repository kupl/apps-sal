class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if ages == []:
            return 0
        ages.sort()
        res = 0
        for i in range(len(ages) - 1, -1, -1):
            if ages[i] < 15:
                break
            age = ages[i]
            left = self.binary_search_left(ages, 0, i, age // 2 + 8)
            right = self.binary_search_right(ages, i, len(ages) - 1, age)
            #print(left, right)
            res += max(0, right - left)
        return res

    def binary_search_left(self, ages, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if ages[mid] < target:
                start = mid
            else:
                end = mid

        if ages[start] >= target:
            return start
        if ages[end] >= target:
            return end
        return -1

    def binary_search_right(self, ages, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if ages[mid] <= target:
                start = mid
            else:
                end = mid
        if ages[end] <= target:
            return end
        if ages[start] <= target:
            return start
        return -1
