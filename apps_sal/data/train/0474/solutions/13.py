class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        limit = Counter(letters)
        n = len(words)
        subsets = []
        def back(i,curr):
            if i==n:
                subsets.append(curr)
                return
            back(i+1, curr+words[i])
            back(i+1, curr)
        back(0,'')
        print(subsets)
        ans = 0
        
        def findscore(wo):
            freq = Counter(wo)
            currscore = 0
            for c in freq:
                if freq[c]<=limit[c]:
                    currscore+=score[ord(c)-ord('a')]*freq[c]
                else:
                    return 0
            return currscore
            
        for x in subsets:
            ans = max(ans, findscore(x))
        return ans
            

