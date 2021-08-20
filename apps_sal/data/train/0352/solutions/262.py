class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def edit_dist(w1, w2):
            n = len(w1)
            m = len(w2)
            if n + 1 != m:
                return False
            mismatch = 0
            i = 0
            j = 0
            while i < n and j < m:
                if w1[i] != w2[j]:
                    mismatch += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            return mismatch <= 1

        def recurse(word, length):
            nonlocal max_l
            max_l = max(max_l, length)
            n = len(word) + 1
            if n in dic:
                for next_word in dic[n]:
                    if edit_dist(word, next_word):
                        recurse(next_word, length + 1)
        dic = collections.defaultdict(list)
        for word in words:
            dic[len(word)].append(word)
        max_l = 0
        for word in words:
            recurse(word, 1)
        return max_l
