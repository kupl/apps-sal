def walk_divisions(string, covered, cut):
    if cut == len(string):
        yield len(covered)
    else:
        for nxt in range(cut + 1, len(string) + 1):
            substring = string[cut:nxt]
            if substring not in covered:
                covered.append(substring)
                yield from walk_divisions(string, covered, nxt)
                covered.pop()


def max_unique_split(string):
    if len(string) == 1:
        return 1
    assert len(string) >= 2
    return max(walk_divisions(string, [], 0))


class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        return max_unique_split(s)
