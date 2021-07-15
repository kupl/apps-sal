class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = len(people)
        end = len(people) - 1
        begin = 0
        res = 0
        while count > 0:
            if people[end] + people[begin] <= limit:
                res+=1
                count-=2
                end-=1
                begin+=1
            else:
                res+=1
                count-=1
                end-=1
        return res
