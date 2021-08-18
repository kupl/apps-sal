

from collections import defaultdict


class Solution(object):
    def uniqueLetterString(self, S):
        dictionary = dict()

        for i in range(len(S)):
            if dictionary.get(S[i]):
                dictionary[S[i]].append(i)
            else:
                dictionary[S[i]] = [i]
        position = dict()
        for letter in dictionary.keys():
            position[letter] = 0
        result = 0
        for index, letter in enumerate(S):
            i = position[letter]
            if i - 1 >= 0:
                l = dictionary[letter][i - 1] + 1
            else:
                l = 0
            if i + 1 <= len(dictionary[letter]) - 1:
                r = dictionary[letter][i + 1] - 1
            else:
                r = len(S) - 1

            result += ((index - l + 1) * (r - index + 1)) % 1000000007
            position[letter] += 1
        return result % 1000000007
