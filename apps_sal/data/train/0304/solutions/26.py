import collections


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = collections.Counter(ages)
        res = 0
        for age_A, count_A in age_count.items():
            for age_B, count_B in age_count.items():
                if not age_B <= age_A * 0.5 + 7 and not age_B > age_A:
                    if age_A == age_B:
                        res += count_A * (count_A - 1)
                    else:
                        res += count_A * count_B
        return res
