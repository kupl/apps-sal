class Solution:

    def longestPrefix(self, s: str) -> str:
        answer = ''
        for n in range(1, len(s)):
            prefix = s[:n]
            suffix = s[-n:]
            if prefix == suffix:
                answer = prefix
        return answer
