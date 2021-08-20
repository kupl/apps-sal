class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        nums = [0] * 121
        for age in ages:
            nums[age] += 1
        ans = 0
        request = [set() for i in range(121)]
        for i in range(1, 121):
            for j in range(1, 121):
                if not (j <= i // 2 + 7 or j > i or (j > 100 and i < 100)):
                    request[i].add(j)
        for i in range(1, 121):
            for j in request[i]:
                ans += nums[i] * (nums[j] if i != j else nums[j] - 1)
        return ans
