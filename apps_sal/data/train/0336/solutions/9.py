class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return 0
        hash_map = dict()
        count = 0
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
        
        for char in t:
            if hash_map.get(char, 0) > 0:
                hash_map[char] -= 1
            else:
                count += 1
        return count
