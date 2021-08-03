class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        count = collections.Counter(s)
        stack = []
        visited = set()
        for c in s:
            count[c] -= 1
            if c in visited:
                continue
            visited.add(c)
            while stack and stack[-1] > c and count[stack[-1]] > 0:
                visited.remove(stack[-1])
                stack.pop()
            stack.append(c)

        return ''.join(stack)
