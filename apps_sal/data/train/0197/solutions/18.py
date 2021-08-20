class Solution:

    def isValid(self, s: str) -> bool:
        cnt = collections.Counter()
        stack = []
        for c in s:
            cnt[c] += 1
            if not cnt['a'] >= cnt['b'] >= cnt['c']:
                return False
            stack.append(c)
            while len(stack) >= 3 and stack[-1] == 'c' and (stack[-2] == 'b') and (stack[-3] == 'a'):
                for _ in range(3):
                    stack.pop()
        if stack:
            return False
        else:
            return True
