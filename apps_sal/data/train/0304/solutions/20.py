from collections import Counter
import math


class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        count = 0
        for age_A in ages:
            max_age = age_A
            min_age = 0.5 * age_A + 7
            for age_B in range(math.floor(min_age) + 1, max_age + 1):
                count += counter[age_B]
                if age_B == age_A:
                    count -= 1
        return count
