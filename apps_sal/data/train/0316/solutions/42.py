class Solution:
    def longestPrefix(self, s: str) -> str:

        def build():
            hashtable = [0 for _ in s]

            for i in range(1, len(s)):
                j = hashtable[i - 1]

                while j > 0 and s[i] != s[j]:
                    j = hashtable[j - 1]

                if s[i] == s[j]:
                    hashtable[i] = j + 1

            return hashtable

        table = build()

        return s[len(s) - table[-1]:]
