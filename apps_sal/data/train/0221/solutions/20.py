class Solution:
    def longestDupSubstring(self, S: str) -> str:
        self.s=S
        self.n=len(S)
        def find_len_k_dup(length):
            hash_value = 0
            mod_value = 8000*(2**30) # a big number should be okay, if you change the number it might cause a wrong answer
            seen = set()
            for i in range(length):
                hash_value = (hash_value*26+ord(self.s[i])-ord('a'))%mod_value # get the hash value
            seen.add(hash_value)
            tmp = pow(26, length)%mod_value
            for i in range(1,self.n-length+1):
                # get the moving hash 
                hash_value = ((hash_value*26 - (ord(self.s[i-1])-ord('a'))*tmp)%mod_value+ord(self.s[i+length-1])-ord('a'))%mod_value
                if hash_value in seen:
                    return i
                else:
                    seen.add(hash_value)
            return None
                
        
        low=0
        high=len(S)
        res=''
        while low<high:
            
            mid=(low+high)//2
            idx=find_len_k_dup(mid)
            #print(candidate)
            if idx is not None:
                res=S[idx:idx+mid]
                low=mid+1
            else:
                high=mid
        return res
