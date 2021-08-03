class Solution:
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
