class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dictByLen = collections.defaultdict(list)
        wordCounter = {}
        
        for i,w in enumerate(words):
            dictByLen[len(w)].append(w)
            wordCounter[w] = collections.Counter(w)
            
        def isOneDiff(s1, s2):
            diff = 0
            j = 0
            for c in s2:
                if c != s1[j]:
                    if diff == 1:
                        return False
                    diff += 1
                else:
                    j += 1
                    if j == len(s1):
                        return True
            return True
                    
        sortedLens = sorted(dictByLen.keys())  
        longestLen = 1
        
        
        prevLen = -1
        
        for l in sortedLens:
            if prevLen == -1 or l != (prevLen + 1):
                prevArr = [(s,1) for s in dictByLen[l]]
            else:
                newArr = []
                
                for s2 in dictByLen[l]:
                    diff = 1
                    for s1, lsf in prevArr:
                        if isOneDiff(s1, s2):
                            diff = max(diff, lsf + 1)
                            
                    newArr.append((s2, diff))
                    longestLen = max(diff, longestLen)
                prevArr = newArr
            prevLen = l
        
        return longestLen
                
            
        

                
                                
                        
            

