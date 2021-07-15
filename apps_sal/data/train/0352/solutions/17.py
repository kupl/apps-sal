class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # group by length
        length2words = defaultdict(list)
        for w in words:
            length2words[len(w)].append(w)
    
        # for each length l -> check words in previous l-1 that form longer chain
        word2chain = {w: 1 for w in words}
        for l in sorted(length2words):
            if l-1 not in length2words:
                continue
            for w in length2words[l]:
                for prev_w in length2words[l-1]:
                    if word2chain[prev_w]+1 < word2chain[w]:
                        continue
                    if self.isPredecessor(prev_w, w):
                        word2chain[w] = max(word2chain[w], word2chain[prev_w]+1)
        
        return max(word2chain.values())
        
    def isPredecessor(self, word1, word2):
        # try skip letter in word2
        for i in range(len(word2)):
            skip = word2[:i]+word2[i+1:]
            if skip == word1:
                return True
        return False
