class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        nboats = 0
        people.sort(reverse=True)
        l = 0
        r = len(people) - 1
        while l < r:
            if people[l] + people[r] > limit:
                l += 1
                nboats += 1
                if l == r:
                    nboats += 1
                    break
            else:
                l += 1
                r -= 1
                nboats += 1
                if l == r:
                    nboats += 1
                    break

        return nboats
