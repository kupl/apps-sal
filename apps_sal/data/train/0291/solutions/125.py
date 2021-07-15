class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        s = [0, 0]
        res = 0
        cur = 0
        for x in arr:
            cur = (cur + x) % 2
            res += s[1-cur]
            res += int(cur == 1)
            s[cur] += 1
        return res % (10 ** 9 + 7)
