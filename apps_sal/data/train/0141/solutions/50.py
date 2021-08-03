class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people) - 1
        boats = 0

        while lo <= hi:
            cap = limit
            cap -= people[hi]  # always take the higher one first
            hi -= 1

            if people[lo] <= cap:  # if you can take a lower one to pair with higher, then include it
                lo += 1

            boats += 1  # increment boat by 1, whether you can only take hi or lo + hi

        return boats
