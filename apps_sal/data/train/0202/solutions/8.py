class Solution:
    def longestMountain(self, a: List[int]) -> int:
        ml = 0
        i = 0
        while(i<len(a)):
            c = 0
            if i+1<len(a) and a[i+1]>a[i]:
                c = 1
                while(i+1<len(a) and a[i+1]>a[i]):
                    c = c + 1
                    i = i + 1
                while(i+1<len(a) and a[i+1]<a[i]):
                    c = c + 1
                    ml = max(c,ml)
                    i = i + 1
            else:
                i = i + 1
        return ml
                    

