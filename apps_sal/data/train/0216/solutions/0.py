class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) % 5 != 0 or croakOfFrogs[0] != 'c' or croakOfFrogs[-1] != 'k':
            return -1
        letters = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        frogs = 0
        temp = 0
        for l in croakOfFrogs:
            letters[l] += 1
            temp = letters['c'] - letters['k']
            if temp > frogs:
                frogs = temp
        c_count = letters['c']
        for letter in letters:
            if letters[letter] != c_count:
                return -1
        return frogs
