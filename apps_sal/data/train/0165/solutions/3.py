class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        word_dict = collections.defaultdict(list)
        for i, word in enumerate(d):
            word_dict[word[0]].append((i, word))

        res = ""
        for c in s:
            words_startswithc = word_dict[c]
            word_dict[c] = []
            for i, word in words_startswithc:
                if len(word) == 1:
                    if len(d[i]) == len(res):
                        res = min(res, d[i])
                    else:
                        res = d[i] if len(d[i]) > len(res) else res
                else:
                    word_dict[word[1]].append((i, word[1:]))
        return res
