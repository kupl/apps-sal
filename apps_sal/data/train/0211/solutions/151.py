class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)
        res = 0

        def findSplit(num):
            bin_str = (bin(num)[2:] + '0').zfill(N)
            words = []
            word = []

            for c, binary in zip(s, bin_str):
                word.append(c)
                if binary == '1':
                    words.append(''.join(word))
                    word = []

            if word:
                words.append(''.join(word))
            return len(set(words))

        ways = 2 ** (N - 1)
        for i in range(ways):
            res = max(res, findSplit(i))

        return res
