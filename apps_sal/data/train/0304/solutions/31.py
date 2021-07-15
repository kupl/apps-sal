class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        ages.sort()
        for i, age in enumerate(ages):
            minTarget = (age // 2) + 7
            maxTarget = age
            minIdx = self.binFinder(ages, minTarget)
            maxIdx = self.binFinder(ages, maxTarget)
            count += max(0, maxIdx - minIdx -1)
        return count
    def binFinder(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + ((right - left)//2)
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left
