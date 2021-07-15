class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        arr = [0 for i in range(n)]
        
        i = 1
        j = 0
        try:
            while i<n:
                if j==0 and s[i]!=s[j]:
                    arr[i] = 0
                    i+=1
                else:
                    if s[i]==s[j]:
                        arr[i] = j+1
                        i+=1
                        j+=1
                    else:
                        j = arr[j-1]

            return s[:arr[n-1]]
        
        except:
            return i
        
    '''
    a a b a a b a a a
    0 1 2 3 4 5 6 7 8
    0 1 0 1 2 3 4 5 2
    
    '''
