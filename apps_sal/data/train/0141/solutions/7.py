class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        length = len(people)
        people.sort()
        left = 0
        right = length - 1
        boat_num = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boat_num += 1
        return boat_num
