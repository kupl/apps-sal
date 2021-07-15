class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        p1 = 0
        
        p2 = len(people) - 1
        
        boat = 0
        
        while p1 <= p2:
            boat+= 1
            if people[p1] + people[p2] <= limit:
                p1 += 1
            
            p2 -= 1
        
        return boat
