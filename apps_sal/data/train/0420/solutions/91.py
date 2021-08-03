class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531840/JavaC%2B%2BPython-One-Pass
        # https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/discuss/531930/This-problem-should-be-marked-as-hard
        aeiou = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4
        }
        seen = {0: -1}
        res = curr = 0
        for i, c in enumerate(s):
            curr ^= 1 << (aeiou.get(c, -1) + 1) >> 1
            seen.setdefault(curr, i)
            res = max(res, i - seen[curr])
        return res
