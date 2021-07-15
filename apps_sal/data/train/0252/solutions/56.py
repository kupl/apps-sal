class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # max_right from each point
        max_right = [0] * (n+1)
        for i, x in enumerate(ranges):
            l = max(0, i-x)
            r = min(n, i+x)
            max_right[l] = r
        # jump game
        ans = 0
        curr_reach = max_reach = 0
        print(max_right)
        for i in range(n+1):
            max_reach = max(max_reach, max_right[i])
            if i == curr_reach:
                print((i, curr_reach, max_reach))
                curr_reach = max_reach
                ans += 1
                if curr_reach == n:
                    return ans
        return ans if curr_reach >= n else -1

