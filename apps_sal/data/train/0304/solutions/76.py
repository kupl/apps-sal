class Solution:

    # problem: https://leetcode.com/problems/friends-of-appropriate-ages/
    # refered the solution in : https://leetcode.com/problems/friends-of-appropriate-ages/discuss/837786/Binary-Search-beating-100-with-detail-explanation

    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        right_most = {}
        for ix, x in enumerate(ages):
            right_most[x] = ix

        l = 0
        count = 0
        for ix, x in enumerate(ages):
            while ages[l] <= (x / 2 + 7) and l < right_most[x]:
                l += 1
            count += right_most[x] - l
        return count
