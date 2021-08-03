class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if n == 1:
            if k < 4:
                return ['a', 'b', 'c'][k - 1]
            else:
                return ''
        ordered = []

        def is_valid(s):
            if s[len(s) - 1] == s[len(s) - 2]:
                return False
            return True
        queue = ['a', 'b', 'c']
        j = 0
        while queue:
            if len(queue[len(queue) - 1]) == n + 1:
                break
            element = queue.pop(0)
            for char in ['a', 'b', 'c']:
                if is_valid(element + char):
                    if len(element + char) == n:
                        ordered.append(element + char)
                    queue.append(element + char)
        if k > len(ordered):
            return ''
        return ordered[k - 1]
