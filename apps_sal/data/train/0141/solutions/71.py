class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        minBoats = 0
        people.sort()
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                minBoats += 1
                left += 1
                right -= 1
            elif people[left] + people[right] > limit:
                minBoats += 1
                right -= 1
        return minBoats
