class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        ## save remainder in hashmap and then check if remaining remainder is in the hashmap
        if len(arr)%2==1:
            return False
        mapping = defaultdict(int)
        count=0
        for i in arr:
            key = k-i%k
            print(key)
            if key in mapping and mapping[key] >=1:
                mapping[key]-=1
                count+=1
            else:
                mapping[(i%k) or k] +=1
                
            
            
        
        
                
        if count ==len(arr)//2:
            return True
        return False
                

