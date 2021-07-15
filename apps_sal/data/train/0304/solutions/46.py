class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def helper(a,b):
            tmpB = a*0.5+7
            return 0 if b<=tmpB or b>a or (b>100 and a<100) else 1
        res,n = 0,len(ages)
        if n == 1:
            return res
        counts = Counter(ages)
        for ageA in counts:
            for ageB in counts:
                countA,countB = counts[ageA],counts[ageB]
                if helper(ageA,ageB):
                    res += countA*countB
                    if ageA == ageB:
                        res -= countA
        return res
