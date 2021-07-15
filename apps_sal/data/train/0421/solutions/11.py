class Solution:
    def lastSubstring(self, s: str) -> str:
        # i: starting index of the first substring
        i = 0
        # j: starting index of the second substring
        j = 1
        # k: length of substring
        k = 0
        
        # the answer must be a consecutive substring start of biggest char
        # if j find better starting index, use it to update i
        n = len(s)
        
        while j+k < n:
            ## cannot compare now, compare at next char
            if s[i+k] == s[j+k]:
                k+=1
                continue
            ## i is bigger, j should find next candidate
            elif s[i+k] > s[j+k]:
                j = j+k+1
            else:
            ## j is bigger, i should find next candidate
                i = i+k+1
            if i == j:
            ## update i with j, j keep searching
                j += 1
            k = 0
        return s[i:]
