class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        s = [0] * 121
        for a in ages:
            count[a] += 1
        for i in range(1, 121):
            s[i] = s[i - 1] + count[i]
        res = 0
        for i in range(15, 121):
            edge = i // 2 + 7
            num = s[i] - s[edge]
            res += count[i] * num - count[i]
        return res
