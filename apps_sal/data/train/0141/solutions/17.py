class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        count = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            cur = people[left] + people[right]
            if cur <= limit:
                left += 1
                right -= 1
            elif cur > limit:
                right -= 1
            count += 1
        return count
