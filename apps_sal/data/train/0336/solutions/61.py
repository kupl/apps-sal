class Solution:

    def minSteps(self, s: str, t: str) -> int:
        help_dict = defaultdict(int)
        res = 0
        for char in s:
            help_dict[char] += 1
        for char in t:
            if help_dict[char] > 0:
                help_dict[char] -= 1
            else:
                res += 1
        return res
