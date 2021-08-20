class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def compare(s1, s2):
            if abs(len(s1) - len(s2)) != 1:
                return False
            if len(s2) > len(s1):
                (s1, s2) = (s2, s1)
            broke = False
            (s1, s2) = (list(s1), list(s2))
            while s1 and s2:
                (a, b) = (s1.pop(), s2.pop())
                if a != b:
                    if broke or s1.pop() != b:
                        return False
                    broke = True
            return True
        G = collections.defaultdict(list)
        i = float('inf')
        j = float('-inf')
        for w in words:
            i = min(i, len(w))
            j = max(j, len(w))
            G[len(w)].append((w, 1))
        res = 1
        m = i + 1
        while m <= j:
            for (a, w1) in enumerate(G[m]):
                for (b, w2) in enumerate(G[m - 1]):
                    if compare(w1[0], w2[0]):
                        G[m][a] = (w1[0], 1 + w2[1])
                        res = max(1 + w2[1], res)
            m += 1
        return res
