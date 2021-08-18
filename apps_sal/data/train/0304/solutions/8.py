'''
    a -> b if
    a = 10
    b = 12
    b > a
    a = 50
    b = 30
    
    a = 50
    b = 50
    .5 * 50 + 7 = 32
    a -> b if a >= b and b > 0.5 * a + 7
    a > 0.5 * a + 7
    0 > 0.5*a + 7 - a
    0 > 7 - .5a
    .5a > 7
    a > 14
    mutual friend request if a > 14
    
    [20, 20, 18, 18, 14, 12 ]
    15 * .5 + 7 = 14.5
    14 * .5 + 7 = 14
    12 * .5 + 7 = 13
    20 * .5 + 7 = 17
    18 * .5 + 7 = 16
    {
    16: 1
    17: 2
    18: 4
    19: 2
    20: 4
    }
    num_reqs = 8, 
    [102, 98, 59]
    102 * .5 + 7 = 58
    59
    98 * .5 + 7 = 56
    {56: 1, 57: 1, 58: 1, 59: 2,...98: 3,...102: 2}
    3
    O(nlogn)
    O(1)
'''


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def invert(a):
            return -1 * a
        ages.sort(key=invert)
        age_request_map = collections.defaultdict(int)
        num_requests = 0
        for age in ages:
            if age <= 14:
                break
            num_requests += age_request_map[age]
            age_request_map[age] += 1
            lowest_age = floor(age * .5 + 7) + 1
            for i in range(lowest_age, age + 1):
                age_request_map[i] += 1
        return num_requests
