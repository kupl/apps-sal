class Solution:
    def removeDuplicateLetters(self, s):
        if not s or len(s) <= 1:
            return s

        from collections import Counter
        count = Counter(s)
        seen = set([])
        stack = []

        i = 0
        while i < len(s):
            char = s[i]
            if char not in seen:
                if stack and ord(stack[-1]) > ord(char) and count[stack[-1]] >= 1:
                    ele = stack.pop()
                    seen.remove(ele)
                else:
                    count[char] -= 1
                    seen.add(char)
                    stack.append(char)
                    i += 1
            else:
                count[char] -= 1
                i += 1

        return ''.join(stack)
