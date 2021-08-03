class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        some_strings = set()
        for i in range(len(text)):
            for j in range(i):
                if text.startswith(text[j:i], i):
                    some_strings.add(text[j:i])
        return len(some_strings)
