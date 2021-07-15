class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        lo = 0 
        hi = len(people) - 1
        count = 0
        
        while lo <= hi:
            count += 1
            if people[lo] + people[hi] <= limit:
                lo += 1
            hi -= 1
            
        return count
        

