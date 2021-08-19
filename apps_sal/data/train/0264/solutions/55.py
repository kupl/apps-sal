class Solution:

    def maxLength(self, arr):

        def isValid(chars):
            if len(chars) == len(set(chars)):
                return True
            else:
                return False
        result = 0
        currentSubset = set()

        def iterate(idx):
            nonlocal result, currentSubset
            if idx == len(arr):
                candidateSolution = ''.join(currentSubset)
                if isValid(candidateSolution) and len(candidateSolution) > result:
                    result = len(candidateSolution)
                return
            currentSubset.add(arr[idx])
            iterate(idx + 1)
            currentSubset.remove(arr[idx])
            iterate(idx + 1)
        iterate(0)
        return result
