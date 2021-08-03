def binary_strings(k):
    res = []
    stack = ['']
    while stack:
        s = stack.pop()
        if len(s) == k:
            res.append(s)
        else:
            stack.append(s + '0')
            stack.append(s + '1')
    return res


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for i in range(0, len(s) - k + 1):
            seen.add(s[i:i + k])
        for bs in binary_strings(k):
            if bs not in seen:
                return False
        return True
