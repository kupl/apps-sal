class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = 'croak'
        frogs = 0
        openCroaks = list()
        char2count = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        for char in croakOfFrogs:
            if char not in croak:
                return -1
            if char == 'c':
                char2count[char] += 1
            elif char2count[croak[croak.find(char) - 1]] > 0:
                char2count[croak[croak.find(char) - 1]] -= 1
                if char != 'k':
                    char2count[char] += 1
            else:
                return -1
            frogs = max(frogs, sum(char2count.values()))
        return frogs if sum(char2count.values()) == 0 else -1
