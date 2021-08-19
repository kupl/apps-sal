import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        max_occur = 0
        freq_hash = {}
        for i in range(len(s) - minSize + 1):
            stri = s[i: i + minSize]
            if len(collections.Counter(stri)) <= maxLetters:
                if stri in freq_hash:
                    freq_hash[stri] += 1
                else:
                    freq_hash[stri] = 1
                max_occur = max(max_occur, freq_hash[stri])
        return max_occur
        # counts = dict()
        # for j in range(len(s)-minSize+1):
        #     word = s[j:j+minSize]
        #     if word in counts:
        #         counts[word]+=1
        #     else:
        #         if len(collections.Counter(word))<=maxLetters:
        #             counts[word]=1
        # return max(counts.values()) if len(counts)!=0 else 0
