class Solution:

    def isValid(self, s: str) -> bool:
        d = []
        for i in s:
            if i == 'c':
                if d[-2:] != ['a', 'b']:
                    return False
                d.pop()
                d.pop()
            else:
                d.append(i)
        return not d
