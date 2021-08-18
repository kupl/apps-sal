class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        if not s:
            return ''

        stack = []

        prev = count = None
        for i in range(0, len(s)):

            if not prev:
                prev, count = s[i], 1
            elif s[i] == prev:
                count += 1
            else:
                stack.append((prev, count))
                prev = s[i]
                count = 1

            if count == k:
                if stack:
                    prev, count = stack.pop()
                else:
                    prev = None

        stack.append((prev, count))

        output = ''
        for e, c in stack:
            output += e * c

        return output


'''
'''
