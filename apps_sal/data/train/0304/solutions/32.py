
import math


def count_smaller_than(ages, target):
    left = 0
    right = len(ages) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if ages[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        ages.sort()
        friend_requests = 0

        for i in range(len(ages)):
            age_a = ages[i]

            smaller_than = count_smaller_than(ages, math.floor(0.5 * age_a) + 8)
            smaller_than_i = count_smaller_than(ages, age_a + 1)

            a_requests = max(0, smaller_than_i - 1 - smaller_than)

            friend_requests += a_requests

        return friend_requests
