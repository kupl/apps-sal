class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0]*k
        for num in arr:
            cnt[num%k] +=1
        i,j = 1,k-1
        pairs = 0
        while i<j:
            if cnt[i]!=cnt[j]:
                return False
            pairs += cnt[i]
            i +=1
            j -=1
            
        if pairs>0 and i==j:
            pairs += cnt[i]/2
        pairs += cnt[0]/2
        n = len(arr)
        return pairs == n//2

