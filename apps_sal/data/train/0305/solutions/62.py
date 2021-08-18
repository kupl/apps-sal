class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        if len(set(text)) == 1:
            return len(text) // 2

        presum = [0]
        for char in text:
            presum.append(presum[-1] + ord(char))

        res = set()
        for w in range(1, len(text) // 2 + 1):
            for i in range(len(text) + 1 - 2 * w):
                if presum[i + w] - presum[i] == presum[i + 2 * w] - presum[i + w]:
                    if text[i:i + w] == text[i + w:i + 2 * w]:
                        res.add(text[i:i + w])

        return len(res)
