class Solution:
    def lastSubstring(self, s: str) -> str:
        # we will be calling this a lot
        lenS = len(s)
        
        # find the lexicographically biggest character
        largestChar = max(set(s))
        
        # find the start of potential max substrings and store in candidates
        # also, make sure to ignore repeats (i.e. aaaaaaaaa.....)
        candidateIndexes = []
        repeating = False
        for i in range(lenS):
            if s[i] == largestChar:
                if repeating == False:
                    candidateIndexes.append(i)
                    repeating = True
            else:
                repeating = False
        
        # go through the candidates, see which one is the best
        bestCandidateIndex = candidateIndexes[0]
        for i in range(1, len(candidateIndexes)):
            counter = 1
            index = candidateIndexes[i]
            while bestCandidateIndex + counter < lenS and index + counter < lenS:
                if s[index + counter] > s[bestCandidateIndex + counter]:
                    bestCandidateIndex = index
                    break
                elif s[index + counter] == s[bestCandidateIndex + counter]:
                    counter += 1
                    continue
                else:
                    break
            
        return s[bestCandidateIndex:]
