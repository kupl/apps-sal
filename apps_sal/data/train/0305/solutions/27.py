class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        text += '.'
        seen = set()
        for k in range(1, n // 2 + 1):
            same = sum(c == d for c, d in zip(text, text[k: k + k]))
            for i in range(n - 2 * k + 1):
                if same == k:
                    seen.add(text[i: i + k])
                same += (text[i + k] == text[i + k * 2]) - (text[i] == text[i + k])
        return len(seen)
        # n = len(text)
        # seen = set()
        # for i in range(n):
        #     for j in range(i + 1, n + 1):
        #         if not (j - i) % 2 and text[i: i + (j - i) // 2] == text[i + (j - i) // 2: j]:
        #             seen.add(text[i: j])
        # return len(seen)

