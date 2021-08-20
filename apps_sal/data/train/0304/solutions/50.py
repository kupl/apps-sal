import math
from collections import Counter


class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        sol = 0
        c = Counter(ages)
        smaller_equal_age = [0]
        for i in range(1, 121):
            smaller_equal_age.append(smaller_equal_age[-1] + c[i])
        for i in range(15, 121):
            sol += c[i] * (smaller_equal_age[i] - 1 - smaller_equal_age[math.floor(0.5 * i + 7)])
        return sol
