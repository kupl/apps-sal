from functools import lru_cache


def _helper(s: str, visited) -> int:
    # s: remaining string to be split
    # count: number of unique pieces already
    # visited: set of string that already be used
    # Returns: the maximum number of unique
    # string pieces we can get

    # Iterate the first split point.
    n = len(s)
    result = 0
    for i in range(n - 1):
        # Cut after i-th char.
        cut, remain = s[:(i + 1)], s[(i + 1):]
        if cut in visited:
            continue
        visited.add(cut)
        result = max(result, 1 + _helper(remain, visited))
        visited.remove(cut)

    # Another option is no cutting
    if not s in visited:
        result = max(result, 1)
    return result


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # DFS/Backtracking,
        # Consider caching to reduce the change of TLE

        if not s:
            return 0

        visited = set()
        return _helper(s, visited)
