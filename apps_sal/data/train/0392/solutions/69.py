class Solution:
    def numWays(self, s: str) -> int:
        l = len(s)
        total_cnt = 0
        for i in range(l):
            if s[i] == '1':
                total_cnt += 1
        if total_cnt % 3:
            return 0
        
        cnt = total_cnt // 3
        if total_cnt == 0:
            return ((len(s) - 1) * (len(s) - 2) // 2) % (10**9 + 7)
        
        c1, c2 = 1, 1
        s1, s2 = s, s[::-1]
        idx = 0
        i1 = self.findIdx(s1, cnt)
        i2 = self.findIdx(s2, cnt)
        
        while s1[i1] != '1':
            c1 += 1
            i1 += 1
        while s2[i2] != '1':
            c2 += 1
            i2 += 1
        return c1 * c2 % (10**9 + 7)
        

    def findIdx(self, s, cnt):
        c, idx = 0, 0
        while idx < len(s) and c < cnt:
            if s[idx] == '1':
                c += 1
            idx += 1
        
        return idx
    
            
    

