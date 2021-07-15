class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        a = [set(i) for i in arr if len(set(i))==len(i)]
        n = len(a)
        an = 0
        for v in range(1, 2**n):
            s=set()
            i=0
            while v>0:
                if v&1 == 1:
                    if s&a[i]: break
                    s=s^a[i]
                v=v>>1
                i+=1
            an = max(an,len(s))
            
        return an
