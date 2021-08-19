class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        graph = collections.defaultdict(list)
        maxlen = float('-inf')
        minlen = float('inf')
        for word in words:
            graph[len(word)].append(word)
            maxlen = max(maxlen, len(word))
            minlen = min(minlen, len(word))

        def predecessor(word1, word2):
            if len(word1) + 1 != len(word2):
                return False
            if not word1:
                return True
            fill = 1
            (left, right) = (0, 0)
            while left < len(word1) and right < len(word2):
                if word1[left] != word2[right]:
                    if fill:
                        right += 1
                        fill -= 1
                        continue
                    else:
                        return False
                left += 1
                right += 1
            return True

        def chain(length, s=''):
            if length not in graph:
                return 0
            ans = 0
            for w in graph[length]:
                if predecessor(s, w):
                    ans = max(ans, 1 + chain(length + 1, w))
            return ans
        ans = 1
        for l in range(minlen, maxlen + 1):
            for w in graph[l]:
                res = chain(l + 1, w) + 1
                ans = max(ans, res)
        return ans
