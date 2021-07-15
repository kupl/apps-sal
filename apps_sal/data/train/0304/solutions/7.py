class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages or len(ages) < 2: return 0
        res=0
        d=[0]*121
        for age in ages:
            d[age]+=1
        for A in range(121):
            for B in range(121):
                count=0
                if B<=A and B> A//2 +7:
                    count+=d[A]*d[B]
                if A==B and count:
                    count-=d[A]
                res+=count
        return res

