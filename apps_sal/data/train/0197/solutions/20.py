class Solution:
    def isValid(self, s: str) -> bool:
        cnt = collections.Counter()
        stack = []
        for c in s:
            cnt[c] += 1
            if not cnt['a'] >= cnt['b'] >= cnt['c']:
                return False
            stack.append(c)
            while ''.join(stack[-3:]) == 'abc':
                stack = stack[:-3]
        if stack:
            return False
        else:
            return True
