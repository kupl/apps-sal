class Solution:

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        added = set()
        ans = []
        for c in s:
            while len(ans) > 0 and c < ans[-1] and (counter[ans[-1]] > 0) and (c not in added):
                added.remove(ans.pop())
            counter[c] -= 1
            if c not in added:
                ans.append(c)
            added.add(c)
        return ''.join(ans)
