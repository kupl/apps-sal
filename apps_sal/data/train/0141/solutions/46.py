class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        number = 0
        while(left <= right):
            if (left == right):
                number += 1
                break
            if people[left] + people[right] <= limit:

                left = left + 1
            right = right - 1
            number += 1
        return number
