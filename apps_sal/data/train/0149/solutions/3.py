class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s
        stack = [[0, '
        for char in s:
            if char == stack[-1][1]:
                stack[-1][0] += 1
                if stack[-1][0] == k:
                    stack.pop()
            else:
                stack.append([1, char])
        return ''.join(c * k for c, k in stack)
