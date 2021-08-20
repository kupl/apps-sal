class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        ans = 0
        (l, r, N) = (0, 0, len(ages))
        same_count = 0
        while r < N:
            same_count = 1
            while r + 1 < N and ages[r + 1] == ages[r]:
                same_count += 1
                r += 1
            while l < r and ages[l] <= 0.5 * ages[r] + 7:
                l += 1
            if l != r:
                ans += same_count * (r - l)
            r += 1
        return ans
