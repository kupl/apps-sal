class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort(reverse=True)
        res = 0
        print(people)
        l, r = 0, len(people) - 1

        while(l <= r):

            print((l, r))
            remain = limit - people[l]
            res += 1
            l += 1
            if remain - people[r] >= 0:
                remain -= people[r]
                r -= 1

        print(res)

        return res


'''

            
        
        
'''
