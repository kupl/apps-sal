class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s = []
        c = 0
        people.sort(reverse=True)
        
        for i in range(len(people)):
            if s and people[i] < s[-1]:
                s[-1] = s[-1] - people[i]
                s.pop()
            elif s and people[i] == s[-1]:
                s.pop()
            elif s and people[i] > s[-1]:
                s.append(limit - people[i])
                c += 1
            elif people[i] == limit:
                c += 1
            else:
                c += 1
                s.append(limit - people[i])
        
        return c
                

