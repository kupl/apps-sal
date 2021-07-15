class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dict = defaultdict()
        for i in range(lo,hi+1):
            steps=0
            j=i
            while i!=1:
                if i%2==0:
                    i=i//2
                else:
                    i = 3*i + 1
                
                steps+=1
                
            dict[j] = steps
            
        dict = sorted(dict.items(), key=lambda x: x[1])

            
        return dict[k-1][0]
