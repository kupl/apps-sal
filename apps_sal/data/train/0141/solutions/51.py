class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo = 0
        count = 0
        for hi in range(len(people))[::-1]:
            if lo < hi and people[lo] + people[hi] <= limit:
                lo += 1
            if lo == hi:
                return len(people) - hi
                

