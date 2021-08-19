class Solution:

    def distinctEchoSubstrings3(self, text: str) -> int:
        if len(set(text)) == 1:
            return len(text) // 2
        presum = [0]
        for char in text:
            presum.append(presum[-1] + ord(char))
        print(presum)
        res = set()
        for w in range(1, (2 + len(text)) // 2):
            for i in range(len(text) + 1 - 2 * w):
                if presum[i + w] - presum[i] == presum[i + 2 * w] - presum[i + w]:
                    if text[i:i + w] == text[i + w:i + 2 * w]:
                        res.add(text[i:i + w])
        return len(res)

    def distinctEchoSubstrings(self, text: str) -> int:
        result = set()
        size = len(text)
        presum = [0] * size * 2
        for i in range(size):
            presum[i] = presum[i - 1] + ord(text[i])
        for i in range(size):
            for j in range(i + 1, size):
                if presum[j - 1] - presum[i] == presum[j + (j - i) - 1] - presum[j]:
                    if text[i:j] == text[j:j + (j - i)]:
                        result.add(text[i:j])
        print(result)
        return len(result)
