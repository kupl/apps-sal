class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        '''
        time complexity :
            because of sorting O(Nlog(N))
            the second loop is smaller so we ignore it
        
        space complexity:
            because of sorting
            O(N)
        '''
        people.sort()
        left = 0
        right = len(people)-1
        boat_number = 0

        while left <= right:
            if left == right:
                boat_number += 1
                break
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                boat_number+=1
            else:
                right -= 1
                boat_number +=1

        return boat_number
