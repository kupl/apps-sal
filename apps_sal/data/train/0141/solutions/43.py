class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        if len(people) == 0 or len(people) == 1:
            return len(people)
        else:
            lptr = 0
            rptr = len(people) - 1
            count = 0
            while lptr <= rptr:
                if((people[lptr] + people[rptr]) <= limit):
                    count += 1
                    lptr += 1
                    rptr -= 1
                else:
                    rptr -= 1
                    count += 1
            return count
            '''
        people.sort()        
        left = 0
        right = len(people) - 1
        
        counter = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                counter += 1
            else: # people[left] + people[right] > limit:
                right -= 1
                counter += 1
            return counter'''
