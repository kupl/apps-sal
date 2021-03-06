"""class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        total_age = 121
        ageCnt = [0]*total_age
        prefixSum = [0]*total_age
        for age in ages:
            ageCnt[age] += 1
        for i in range(1, total_age):
            prefixSum[i] = ageCnt[i] + prefixSum[i-1]
        res = 0 
        for i in range(15, total_age):
            if ageCnt[i] == 0:
                continue 
            res += ageCnt[i]*(prefixSum[i]-prefixSum[int(i*.5+7)]-1)#)- ageCnt[i]
        return res """


class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        maxAge = 121
        preSum = [0] * maxAge
        from collections import Counter
        ageCnt = Counter(ages)
        for i in range(1, maxAge):
            preSum[i] += preSum[i - 1] + ageCnt[i]
        res = 0
        for age in range(15, maxAge):
            res += (preSum[age] - preSum[int(0.5 * age + 7)] - 1) * ageCnt[age]
        return res
        '\n        Person A will NOT friend request person B (B != A) \n        if any of the following conditions are true:\nage[B] <= 0.5 * age[A] + 7\nage[B] > age[A]\nage[B] > 100 && age[A] < 100\n        '
        'from collections import Counter \n        cnt = Counter(ages)\n        res = 0 \n        def request(a,b):\n            return not (b <= .5*a+7 or b>a)\n        for a in cnt:\n            for b in cnt:\n                res += request(a,b)*cnt[a]*(cnt[b]-(a==b))\n        return res '
