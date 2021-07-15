class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # first start something simple 
        # should be able to do this in O(n) 
        ages.sort()
        ans, i, j = 0, 0, 0
        while i < len(ages): 
            val = ages[i]
            while j < i and ages[j] <= (0.5 * val + 7): 
                j += 1
            cnt, num_equal = i - j, 0
            while i < len(ages) and ages[i] == val: 
                num_equal, i = num_equal + 1, i+1
            # here could be either out of bound of different value
            ans += (num_equal * cnt) + (num_equal * (num_equal-1))
        return ans
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                # if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans
