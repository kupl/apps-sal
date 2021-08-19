class Solution:

    def maxLength(self, arr: List[str]) -> int:
        if arr == None:
            return
        path = []
        result = [0]

        def generateCombinations(arr, i, result, path):
            if i == len(arr):
                if path:
                    combination = ''.join(path)
                    if len(set(combination)) == len(combination):
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
