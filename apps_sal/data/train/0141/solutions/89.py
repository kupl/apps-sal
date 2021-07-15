class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l=0
        r=len(people)-1
        ret=0
        while l<r:
            if people[r]>=limit:
                ret+=1
                r-=1
            elif people[r]+people[l]>limit:
                ret+=1
                r-=1
            else:
                ret+=1
                l+=1
                r-=1
        if l==r:
            ret+=1
        return ret

