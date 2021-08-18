'''

Arr: [16, 16]


Arr: [16, 16, 17, 18]


{16:2, 17: 1, 18:1}

A: 16, B = 17

17 <= 8 + 7

17 <= 15 NOT


{16:2, 17: 1, 18:1}

{16:2, 17: 1, 18:1}

2 + 2 + 0 + 1

[20,30,100,110,120]

{20:1, 30:1, 100:1, 110:1, 120: 1}

{20:1, 30:1, 100:1, 110:1, 120: 1}

20:0
30:1, 30: B, 20: A  30 <= 17
100:0

Solution:

Count the ages. 

* For each age, compare with other ages and figure how many possible matches happen. 
'''
from collections import Counter


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        if not ages:
            return 0

        def friend(A, B):
            if B > A:
                return False
            if B <= (A * 0.5) + 7:
                return False
            return True

        counter = Counter(ages)

        requests = 0

        for ageA, countA in list(counter.items()):
            for ageB, countB in list(counter.items()):
                if friend(ageA, ageB):
                    requests = requests + (countA * countB) if ageA != ageB else requests + (countA - 1) * countA

        return requests
