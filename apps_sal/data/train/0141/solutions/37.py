class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num_boats = 0
        last = len(people) - 1
        first = 0
        while first < last:
            if people[first] + people[last] <= limit:
                last -= 1
                first += 1
                num_boats += 1
            else:
                num_boats += 1
                last -= 1
        if first == last:
            num_boats += 1
        return num_boats
