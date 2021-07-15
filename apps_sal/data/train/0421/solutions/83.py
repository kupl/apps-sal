'''
case 1:
   a b ...
   i j    => change i to j , j to j+1
case 2:
    cbacbd
    i  j => i==j compare next one
    c b   a  c  b   d
    i i+1    j  j+1  => i==j compare next one
    i=2 < j+2
    i = j 
    j = new_i+1 why? allelemnts are smaller than original i 

'''
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0,1,0
        while j+k < len(s):
            if s[i+k] > s[j+k]:
                j = j+k+1
                k = 0
            elif s[i+k] == s[j+k]:
                k += 1
            else:
                i = max(i + k + 1, j)
                j = i+1
                k = 0
        return s[i:]
