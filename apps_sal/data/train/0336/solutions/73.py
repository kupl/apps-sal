class Solution:

    def minSteps(self, s: str, t: str) -> int:
        if s is None or t is None:
            return -1
        hashmap = dict()
        count = 0
        for char in s:
            if char in hashmap:
                hashmap[char] = 1 + hashmap[char]
            else:
                hashmap[char] = 1
        for char in t:
            if char in hashmap:
                if hashmap[char] is not 0:
                    hashmap[char] = hashmap[char] - 1
        for key in hashmap:
            count += hashmap[key]
        return count
