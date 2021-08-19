class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = collections.defaultdict(int)
        mapping = collections.defaultdict(int)
        if len(s) < minSize:
            return 0
        count = 0
        for i in range(minSize):
            mapping[s[i]] += 1
            if mapping[s[i]] == 1:
                count += 1
        if count <= maxLetters:
            counter[s[0:minSize]] += 1
        for i in range(1, len(s) - minSize + 1):
            mapping[s[i - 1]] -= 1
            if mapping[s[i - 1]] == 0:
                count -= 1
            mapping[s[i + minSize - 1]] += 1
            if mapping[s[i + minSize - 1]] == 1:
                count += 1
            # print(s[i:i+minSize])
            if count <= maxLetters:
                counter[s[i:i + minSize]] += 1
        # print(counter)
        if not counter:
            return 0
        return max(counter.values())
