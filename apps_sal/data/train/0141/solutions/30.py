class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        h = len(people) - 1
        remain_capacity = limit
        if len(people) == 0:
            return 0
        boat = 1
        ppl_in_boat = 2
        while l <= h:
            if people[h] <= remain_capacity and ppl_in_boat != 0:
                remain_capacity -= people[h]
                ppl_in_boat -= 1
                h = h - 1
            elif remain_capacity >= people[l] and ppl_in_boat != 0:
                remain_capacity -= people[l]
                ppl_in_boat -= 1
                l = l + 1
            else:
                boat += 1
                remain_capacity = limit
                ppl_in_boat = 2
        return boat
