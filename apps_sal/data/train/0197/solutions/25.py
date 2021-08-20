class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if stack == []:
                stack.append([])
                stack[-1].append(ord(s[i]))
            elif stack[-1][-1] + 1 == ord(s[i]):
                stack[-1].append(ord(s[i]))
            else:
                stack.append([ord(s[i])])
            if stack[-1] == [ord('a'), ord('b'), ord('c')]:
                stack.pop()
        return stack == []
