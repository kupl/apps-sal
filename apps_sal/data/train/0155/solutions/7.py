from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        result = 0
        mapping = dict()
        for index, value in enumerate(arr):
            if index not in mapping:
                mapping[index] = set()
            for dd in range(1, d + 1):
                if index + dd >= len(arr):
                    break

                if arr[index + dd] < arr[index]:
                    mapping[index].add(index + dd)
                else:
                    break

            for dd in range(1, d + 1):
                if index - dd < 0:
                    break

                if arr[index - dd] < arr[index]:
                    mapping[index].add(index - dd)
                else:
                    break
            pass

        cache = dict()

        def dfs(cache, mapping, root):

            if root in cache:
                return cache[root]

            if root not in mapping:
                return 0

            result = 0
            for next in mapping[root]:
                result = max(result, dfs(cache, mapping, next) + 1)
                pass

            cache[root] = result
            return result

        result = 1
        for i in range(len(arr)):
            result = max(result, dfs(cache, mapping, i) + 1)

        return result
