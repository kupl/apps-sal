class Solution:

    def maxLength(self, arr: List[str]) -> int:
        if arr == None:
            return
        path = []
        result = [0]

        def hasUniqueLetters(word):
            hash_set = set()
            for c in word:
                if c in hash_set:
                    return False
                else:
                    hash_set.add(c)
            return True

        def generateCombinations(arr, i, result, path):
            if i == len(arr):
                combination = ''.join(path)
                if path and hasUniqueLetters(combination):
                    if result[0] < len(combination):
                        result[0] = len(combination)
                return
            curr_path = []
            curr_path.extend(path)
            curr_path.append(arr[i])
            generateCombinations(arr, i + 1, result, path)
            generateCombinations(arr, i + 1, result, curr_path)
        generateCombinations(arr, 0, result, path)
        return result[0]
