class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        ans = 0
        while i <= j:
            if i == j:
                return ans + 1
            elif people[i] + people[j] > limit:
                j -= 1
                ans += 1
            else:
                i += 1
                j -= 1
                ans += 1
        return ans
