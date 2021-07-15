class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people, reverse=True)
        boats = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
            boats += 1
        return boats

