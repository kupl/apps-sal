class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        
        def check(a,i):
            if(a == B):
                return 0
            if a[i] != B[i]:
                j=i
                minCount = None
                while(j<len(a)):
                    if a[j] == B[i]:
                        if a[i] == B[j]:
                            return 1 + check(a[:i]+a[j]+a[i+1:j]+a[i]+a[j+1:],i+1)
                        count = check(a[:i]+a[j]+a[i+1:j]+a[i]+a[j+1:],i+1)
                        if minCount == None or minCount > count:
                            minCount = count
                    j+=1
                return 1 + minCount
                        
            else:
                return 0 + check(a,i+1)
            
        return check(A,0)
