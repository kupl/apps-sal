# O(nlogn) time and O(1) space
# Greedy approach: pair the heaviest person with the lightest
# Since there are only 2 people on one boat you don't need to \"optimize\" the space of the boat to carry the third person. Moreover, you can show that if you can pair the heaviest with second heaviest, you can essentially pair any 2 people on the boat (which is the best case scenario).
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            ans += 1

        return ans
