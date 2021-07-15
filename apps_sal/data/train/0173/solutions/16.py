class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = defaultdict(int)
        for x in arr:
            count[x%k] += 1
        
        if 0 in count:
            if count[0]%2:
                return False
            else:
                count.pop(0)
                
        if k%2==0 and k//2 in count:
            if count[k//2]%2:
                return False
            else:
                count.pop(k//2)
            
        while count:
            x = next(iter(count))
            if k-x in count:
                if count[k-x]==count[x]:
                    count.pop(x)
                    count.pop(k-x)
                else:
                    return False
            else:
                return False
        return True
