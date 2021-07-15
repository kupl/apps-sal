class Solution:
    def numSplits(self, s: str) -> int:
        pre = [0] * len(s)
        
        acc = set()
        cnt = 0
        for i in range(len(s) - 1):
            if s[i] not in acc:
                cnt += 1
                acc.add(s[i])
            pre[i] = cnt
        
        cnt = 0
        acc.clear()
        res = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] not in acc:
                cnt += 1
                acc.add(s[i])
            if pre[i - 1] == cnt:
                res += 1
            
        return res
