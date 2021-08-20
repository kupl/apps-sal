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
                if people[lptr] + people[rptr] <= limit:
                    count += 1
                    lptr += 1
                    rptr -= 1
                else:
                    rptr -= 1
                    count += 1
            return count
            '\n        people.sort()        \n        left = 0\n        right = len(people) - 1\n        \n        counter = 0\n        while left <= right:\n            if people[left] + people[right] <= limit:\n                left += 1\n                right -= 1\n                counter += 1\n            else: # people[left] + people[right] > limit:\n                right -= 1\n                counter += 1\n            return counter'
