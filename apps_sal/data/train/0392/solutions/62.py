class Solution:
    def numWays(self, s: str) -> int:
        ones = sum(c == '1' for c in s)
        if ones % 3:
            return 0
        if ones == 0:
            N = len(s) - 2
            return N * (N + 1) // 2 % (10**9 + 7)

        target = ones // 3

        N = len(s)

        left1 = left2 = None
        cnt = 0
        for i, c in enumerate(s):
            if c == '1':
                cnt += 1
            if cnt == target:
                if left1 is None:
                    left1 = i
                left2 = i

        right1 = right2 = None
        cnt = 0
        for i, c in enumerate(s[::-1]):
            if c == '1':
                cnt += 1
            if cnt == target:
                if right1 is None:
                    right1 = N - 1 - i
                right2 = N - 1 - i
        ans = (left2 - left1 + 1) * (right1 - right2 + 1)
        return ans % (10**9 + 7)
