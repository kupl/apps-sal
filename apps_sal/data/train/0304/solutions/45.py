import collections


class Solution:

    # problem: https://leetcode.com/problems/friends-of-appropriate-ages/
    # refered the solution in : https://leetcode.com/problems/friends-of-appropriate-ages/discuss/737217/Python-simple-solution-using-counters-beats-85

    def numFriendRequests(self, ages: List[int]) -> int:

        count = 0  # the number of friend requests

        table = collections.Counter(ages)

        for ageA in table:
            num_ = table[ageA]  # the number age' people
            for ageB in table:
                if ageB <= 0.5 * ageA + 7:
                    continue
                if ageB > ageA:
                    continue
                if ageB > 100 and ageA < 100:
                    continue
                # if the age is not me
                if ageA != ageB:
                    count += num_ * table[ageB]
                else:
                    count += int(num_ * (num_ - 1))

        return count
