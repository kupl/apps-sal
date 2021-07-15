class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t):
            return False
        N=26
        cnt=[0]*N
        for i in range(len(s)):
            if s[i]==t[i]:
                continue
            cnt[(ord(t[i])-ord(s[i]))%N]+=1
        # print(cnt)
        for i in range(1,N):
            if cnt[i]>(k//N)+(k%N >=i):
                return False
        return True
