class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        if len(set(text)) == 1:
            return len(text) // 2  # 1

        presum = [0]  # 2
        for char in text:
            presum.append(presum[-1] + ord(char))

        res = set()
        for w in range(1, (2 + len(text)) // 2):
            for i in range(len(text) + 1 - 2 * w):
                j = i + w
                if presum[j] - presum[i] == presum[j + w] - presum[j]:  # 2.1
                    if text[i:j] == text[j:j + w]:  # 3
                        res.add(text[i:j])

        return len(res)
