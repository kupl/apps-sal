class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if people == None or len(people) == 0:
            return 0
        people.sort()
        start = 0
        end = len(people) - 1
        counter = 0
        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
                end -= 1
            else:
                end -= 1
            counter += 1
        return counter
