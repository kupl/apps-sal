class Solution:
    # O(n^3) time, O(n^2) space
    def distinctEchoSubstrings(self, text: str) -> int:
        
        def is_echo(s):
            n = len(s)
            if n % 2 != 0:
                return False
            return s[: n // 2] == s[n // 2 :]
        
        echo_str_set = set()
        for i in range(len(text)):
            for j in range(i, len(text)):
                substr = text[i : j + 1]
                if is_echo(substr):
                    echo_str_set.add(substr)
        return len(echo_str_set)

