class Solution:

    def lastSubstring(self, s: str) -> str:
        lenS = len(s)
        largestChar = max(set(s))
        candidateIndexes = []
        repeating = False
        for i in range(lenS):
            if s[i] == largestChar:
                if repeating == False:
                    candidateIndexes.append(i)
                    repeating = True
            else:
                repeating = False
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
