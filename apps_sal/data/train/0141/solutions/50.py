class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people) - 1
        boats = 0

        while lo <= hi:
            cap = limit
            cap -= people[hi]
            hi -= 1

            if people[lo] <= cap:
                lo += 1

            boats += 1

        return boats
