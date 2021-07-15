class Solution:
    # O(p + plog(p)) = O(p(1 + log(p))) = O(plog(p)) time / O(1) space or memory
    # where 'p' is the number of people
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # 1st step: sort the array of people's weights
        people.sort()
        
        # 2nd step: get the current lightest person, fit on the boat, then try to 
        # put also the lightest person if possible
        # EACH BOAT CARRIES AT MOST 2 PEOPLE
        nb_of_boats = 0
        i, j = 0, len(people) - 1
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            nb_of_boats += 1
        
        return nb_of_boats
