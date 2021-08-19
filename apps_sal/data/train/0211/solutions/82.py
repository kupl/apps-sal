class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def back(i, curr, addhere):
            if i == n:
                return len(addhere) - 1
            if curr + s[i] in addhere:
                return back(i + 1, curr + s[i], addhere.copy())
            else:
                return max(back(i + 1, '', addhere.union({curr + s[i]})), back(i + 1, curr + s[i], addhere.copy()))
        b = set()
        b.add('')
        return back(0, '', b)
