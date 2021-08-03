class Solution:
    def isValid0(self, S: str) -> bool:

        if len(S) < 3:
            return False

        if len(S) == 3:
            if S == 'abc':
                return True
            else:
                return False

        # find 'abc'
        i = 0
        while i < len(S) and S[i:i + 3] != 'abc':
            i += 1

        if S[i:i + 3] == 'abc':
            new_S = S[:i] + S[i + 3:]
            return self.isValid(new_S)
        else:
            return False

    def isValid(self, S: str) -> bool:

        stack = []
        for c in S:
            if len(stack) < 2:
                stack.append(c)
            else:
                if stack[-2] + stack[-1] + c == 'abc':
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False
