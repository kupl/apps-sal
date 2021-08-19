class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0 for i in range(n + 1)]
        for i in range(n + 1):
            (left, right) = (max(0, i - ranges[i]), min(i + ranges[i], n))
            max_range[left] = max(max_range[left], right - left)
        jumps = 0
        (curlen, endlen) = (0, 0)
        print(max_range)
        for i in range(n + 1):
            if max_range[i] == 0 and endlen < i:
                return -1
            curlen = max(curlen, i + max_range[i])
            if i == endlen:
                endlen = curlen
                jumps += 1
            if endlen == n:
                return jumps
        return jumps
