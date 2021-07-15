class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort list
        # set l = 0, r = last
        # see if l+r will fit in boat
        # if too heavy, put r in boat and iterate r     
        
        nboats = 0
        people.sort(reverse=True)
        l = 0
        r = len(people)-1
        while l < r:
            if people[l]+people[r] > limit:
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
