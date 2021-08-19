class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        res = set()
        text += '.'
        for k in range(1, N // 2 + 1):
            same = sum((a == b for (a, b) in zip(text, text[k:k + k])))
            for i in range(N - 2 * k + 1):
                if same == k:
                    res.add(text[i:i + k])
                same += (text[i + k] == text[i + 2 * k]) - (text[i] == text[i + k])
        return len(res)
