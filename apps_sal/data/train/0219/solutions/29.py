# https://leetcode.com/problems/longest-well-performing-interval/discuss/334565/JavaC%2B%2BPython-O(N)-Solution-Life-needs-996-and-669

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        seen = dict()
        cnt = 0
        res = 0
        for idx, h in enumerate(hours):
            if h > 8:
                cnt += 1
            else:
                cnt -= 1
            if cnt > 0:
                res = idx + 1
            else:
                if cnt - 1 in seen:
                    res = max(res, idx - seen[cnt - 1])
            if cnt not in seen:
                seen[cnt] = idx
        return res
