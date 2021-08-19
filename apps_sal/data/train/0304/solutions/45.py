import collections


class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        table = collections.Counter(ages)
        for ageA in table:
            num_ = table[ageA]
            for ageB in table:
                if ageB <= 0.5 * ageA + 7:
                    continue
                if ageB > ageA:
                    continue
                if ageB > 100 and ageA < 100:
                    continue
                if ageA != ageB:
                    count += num_ * table[ageB]
                else:
                    count += int(num_ * (num_ - 1))
        return count
