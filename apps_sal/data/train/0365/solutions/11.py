class Solution:

    def uniqueLetterString(self, s: str) -> int:
        """
        For each 'char' in string, count the number of substrings contains this 'char' and only one 'char'.
        Time: O(n)
        Space: O(n)
        """

        def count(c, s):
            n = len(s)
            idxes = []
            for i in range(n):
                if s[i] == c:
                    idxes.append(i)
            total = 0
            for (i, idx) in enumerate(idxes):
                left = idx - 0 + 1
                right = n - 1 - idx + 1
                if i:
                    left = idx - idxes[i - 1]
                if i < len(idxes) - 1:
                    right = idxes[i + 1] - idx
                total += left * right
            return total
        chars = set(s)
        ans = 0
        for c in chars:
            ans += count(c, s)
            ans = ans % (10 ** 9 + 7)
        return ans
