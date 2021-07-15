class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = collections.Counter([i%k for i in arr])
        print(c)
        
        for j in c:
            if j == 0:
                if c[j]%2: 
                    return False
            else:
                if c[j]!=c[k-j]:
                    return False
        return True
