class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        res = 0
        i = 0
        while i < len(ages):
            if ages[i] <= 14:
                i += 1
            else:
                break
        if i == len(ages):
            return 0
        leftmost = i
        for i in range(leftmost, len(ages)):
            left, right = leftmost, i - 1
            edge = ages[i] * 0.5 + 7
            while left <= right:
                m = (left + right) // 2
                if ages[m] <= edge:
                    left = m + 1
                else:
                    right = m - 1
            res += i - left
            # find same age:
            left, right = i + 1, len(ages) - 1
            while left <= right:
                m = (left + right) // 2
                if ages[m] <= ages[i]:
                    left = m + 1
                else:
                    right = m - 1
            left -= 1
            res += left - i
        return res
