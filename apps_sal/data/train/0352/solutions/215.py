class Solution:

    def predecessor(self, w1, w2):
        
        i = 0

        diffs = 0

        while i<len(w1):
            if w1[i] != w2[i]:
                diffs = 1
                break

            i+=1

        if diffs==0:
            return True

        return w1==w2[:i]+w2[i+1:]

    def longestStrChain(self, words):

        words = sorted(words, key=lambda x: len(x))

        #print(words)

        words_by_len = {}

        for w in words:
            if len(w) in words_by_len:
                words_by_len[len(w)].append(w)
            else:
                words_by_len[len(w)] = [w]

        #print(words_by_len)

        max_lens = {}

        for w in words:
            max_lens[w] = 1

        for l in words_by_len:

            if l-1 in words_by_len:
            
                for w1 in words_by_len[l]:
                    for w2 in words_by_len[l-1]:
                        #print(w1, w2)

                        if self.predecessor(w2, w1):
                            max_lens[w1] = max(max_lens[w1], 1+max_lens[w2])

        max_len = 0

        for w in max_lens:
            max_len = max(max_len, max_lens[w])

        return max_len


