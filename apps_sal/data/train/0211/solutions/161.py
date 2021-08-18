from functools import lru_cache


def _helper(s: str, visited) -> int:

    n = len(s)
    result = 0
    for i in range(n - 1):
        cut, remain = s[:(i + 1)], s[(i + 1):]
        if cut in visited:
            continue
        visited.add(cut)
        result = max(result, 1 + _helper(remain, visited))
        visited.remove(cut)

    if not s in visited:
        result = max(result, 1)
    return result


class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        if not s:
            return 0

        visited = set()
        return _helper(s, visited)
