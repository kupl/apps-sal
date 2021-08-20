class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        (left, right) = (0, len(people) - 1)
        boats = 0
        while left <= right:
            if left == right:
                boats += 1
                break
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                right -= 1
                boats += 1
        return boats
