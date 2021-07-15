class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first_position = {(0, 0, 0, 0, 0):-1}
        counter = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        ans = 0
        for i, c in enumerate(s):
            if c in counter:
                counter[c]+=1
            key = tuple((counter[c]%2 for c in 'aeiou'))
            if key not in first_position:
                first_position[key] = i
            ans = max(i - first_position[key], ans)
        return ans
