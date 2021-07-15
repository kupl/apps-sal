from collections import Counter 
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        li=collections.Counter([x%k for x in arr])
        for i in li:
            if i==0 or li[i]==0:
                continue
            print((i,li[i]))
            if li[k-i]!=li[i] :
                return False
        if li[0]%2==0:
            return True
        else:
            return False


