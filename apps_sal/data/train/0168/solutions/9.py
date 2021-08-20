class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        dictionary = {}
        for character in s:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
        print(list(dictionary.values()))
        odd_occurences = 0
        for e in list(dictionary.values()):
            if e % 2 == 1:
                odd_occurences += 1
        print(odd_occurences)
        if odd_occurences > k:
            return False
        return True
