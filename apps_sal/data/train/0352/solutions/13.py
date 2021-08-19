class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        hashtable = {}
        record = [1 for i in range(17)]
        for w in words:
            if(len(w) not in hashtable):
                hashtable[len(w)] = [{w: 1}]
            else:
                hashtable[len(w)].append({w: 1})
        # print(hashtable)
        for i in range(17):
            if(i in hashtable):
                if(i - 1 in hashtable):
                    # print(hashtable[i])
                    n = 0
                    tmp_max = 0
                    for word in hashtable[i]:
                        word = list(word.keys())[0]
                        m = 0
                        for preword in hashtable[i - 1]:
                            preword = list(preword.keys())[0]
                            if(self.ispreword(preword, word)):
                                hashtable[i][n][word] = max(hashtable[i - 1][m][preword] + 1, hashtable[i][n][word])
                                tmp_max = max(tmp_max, hashtable[i][n][word])
                            m += 1
                        n += 1
                    record[i] = tmp_max
                    # print( hashtable[i])

        # print(record)
        return max(record)

    def ispreword(self, preword, word):
        check = [i for i in word]
        for w in preword:
            if w not in check:
                return False
            else:
                check.remove(w)
        return True
