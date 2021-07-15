class Solution:
    def int_to_bin(self,x):
        ret=''
        if x==0:
            return '0' 
        while x>0:
            ret=str(x%2)+ret 
            x=x//2 
        return ret
    def queryString(self, S: str, N: int) -> bool:
        mp={} 
        max_len=min(31,len(S)) 
        for k in range(1,max_len+1):
            for i in range(len(S)-k+1):
                mp[S[i:i+k]]=True
        for i in range(1,N+1):
            if self.int_to_bin(i) not in mp:
                return False 
        return True

