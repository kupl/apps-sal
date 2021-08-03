class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        chainLen = {w: 1 for w in words}
        ret = 1
        for i, word1 in enumerate(words):
            for j in range(i + 1, len(words)):
                word2 = words[j]
                if len(word2) == len(word1):
                    continue
                if len(word2) > len(word1) + 1:
                    break
                insert = False
                match = True
                idx1 = 0
                idx2 = 0
                while idx1 < len(word1):
                    if word1[idx1] != word2[idx2]:
                        if insert:
                            match = False
                            break
                        else:
                            insert = True
                            idx2 += 1
                            continue
                    idx1 += 1
                    idx2 += 1
                if match:
                    l = max(chainLen[word2], chainLen[word1] + 1)
                    ret = max(ret, l)
                    chainLen[word2] = l
        return ret
