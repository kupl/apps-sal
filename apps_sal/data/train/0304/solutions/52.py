class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for a in ages:
            count[a] += 1
        for (i, val) in enumerate(count):
            count[i] = count[i - 1] + val
        total = 0
        for a in ages:
            ageMin = floor(0.5 * a + 8)
            ageMax = min(a, 120)
            ageMin = max(ageMin - 1, 0)
            total += max(count[ageMax] - count[ageMin] - 1, 0)
        return total
