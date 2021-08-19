class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def isPredecessor(w1, l1, w2, l2):
            if l2 == l1 + 1:
                for i in w1:
                    if i not in w2:
                        return False
                return True
            return False
        words.sort(key=lambda x: len(x))
        L = [len(i) for i in words]
        DP = [1 for i in range(len(L))]
        ans = 1
        for i in range(1, len(L)):
            for j in range(0, i):
                if isPredecessor(words[j], L[j], words[i], L[i]):
                    DP[i] = max(DP[j] + 1, DP[i])
            ans = max(ans, DP[i])
        return ans
