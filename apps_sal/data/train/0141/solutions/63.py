# 1, 2, 2, 3 limit = 4
# l        r


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        
        left = 0
        right = len(people) - 1
        counter = 0
        while left < right:
            total = people[left] + people[right]
            counter += 1
            right -= 1
            if total <= limit:
                left += 1
        
        if left == right:
            counter += 1
        
        return counter

