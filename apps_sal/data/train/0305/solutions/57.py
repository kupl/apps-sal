class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        prefix_rolling_hash = [0 for _ in range(len(text) + 1)]
        for i in range(len(text)):
            prefix_rolling_hash[i + 1] = ord(text[i]) + prefix_rolling_hash[i]
        res = set()
        for i in range(len(text)):
            for j in range(i):
                if (i - j + 1) % 2 == 0:
                    if prefix_rolling_hash[j + ((i - j + 1) // 2)] - prefix_rolling_hash[j] == prefix_rolling_hash[i + 1] - prefix_rolling_hash[j + ((i - j + 1) // 2)]:
                        x = text[j: (j + (i - j + 1) // 2)]
                        if x == text[(j + (i - j + 1) // 2): i + 1]:
                            res.add(x)
        return len(res)
