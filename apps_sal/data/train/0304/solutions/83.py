class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = collections.Counter(ages)
        
        print(count)
        ans = 0
        
        for ageA in count:
            for ageB in count:
                countA = count[ageA]
                countB = count[ageB]
                if ageB <= ageA*0.5 + 7:
                    continue
                if ageA < ageB:
                    continue
                ans += countA * countB
                if ageA == ageB:
                    ans -= countA
        return ans
