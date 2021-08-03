class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        counter = collections.defaultdict(int)
        longest = 0

        for w in sorted(words, key=len):
            for i in range(len(w)):
                subword = w[:i] + w[i + 1:]
                count = counter[subword] + 1
                counter[w] = max(counter[w], count)
                longest = max(longest, counter[w])

        return longest
