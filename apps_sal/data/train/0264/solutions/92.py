class Solution:

    def maxLength(self, arr: List[str]) -> int:
        letters_dict = {}

        def dfs(letter_set, arr, i):
            if i >= len(arr):
                return 0
            if (tuple(letter_set), i) not in letters_dict:
                if len(set(arr[i]).intersection(letter_set)) == 0 and len(set(arr[i])) == len(arr[i]):
                    letters_dict[tuple(letter_set), i] = max(dfs(letter_set.union(set(arr[i])), arr, i + 1) + len(set(arr[i])), dfs(letter_set, arr, i + 1))
                else:
                    letters_dict[tuple(letter_set), i] = dfs(letter_set, arr, i + 1)
            return letters_dict[tuple(letter_set), i]
        return dfs(set(), arr, 0)
