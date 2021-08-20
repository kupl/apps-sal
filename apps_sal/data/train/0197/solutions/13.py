class Solution:

    def isValid(self, s: str) -> bool:
        cnt = collections.Counter()
        stack = []
        for c in s:
            cnt[c] += 1
            if not cnt['a'] >= cnt['b'] >= cnt['c']:
                return False
            if c == 'c':
                if len(stack) >= 2:
                    if stack[-1] == 'b' and stack[-2] == 'a':
                        stack.pop()
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(c)
        return not stack
