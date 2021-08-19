class Solution:

    def minSteps(self, s: str, t: str) -> int:
        min_steps = 0
        count = collections.Counter(s)
        for char in t:
            if char not in count:
                min_steps += 1
            else:
                count[char] -= 1
                if count[char] == 0:
                    del count[char]
        return min_steps
