class Solution:

    def numSplits(self, string: str) -> int:

        def isValid(string, i):
            return 0 <= i < len(string)

        def getLength(string, unique, i):
            if isValid(string, i):
                unique.add(string[i])
                return len(unique)
            return len(unique)
        (left, right) = ([0] * len(string), [0] * len(string))
        (left_unique, right_unique) = (set(), set())
        reversed_string = string[::-1]
        for i in range(len(left)):
            left[i] = getLength(string, left_unique, i)
            right[len(right) - 1 - i] = getLength(reversed_string, right_unique, i)
        good_splits = 0
        for i in range(len(left) - 1):
            if right[i + 1] == left[i]:
                good_splits += 1
        return good_splits
