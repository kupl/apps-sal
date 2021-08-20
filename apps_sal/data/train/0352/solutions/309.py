class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        lis = defaultdict(int)
        words = sorted(words, key=len)
        print(words)
        ans = 0
        for i in range(n):
            w = words[i]
            for j in range(len(words[i])):
                s = w[0:j] + w[j + 1:]
                lis[w] = max(lis[w], lis[s] + 1)
            ans = max(ans, lis[w])
        return ans
