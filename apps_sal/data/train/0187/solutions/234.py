class Solution:
    def minOperationsMaxProfit(self, c: List[int], b: int, r: int) -> int:
        cnt = 0
        p = 0
        m = 0
        mi = -1
        ind = 0
        for i,cc in enumerate(c):
            cnt+=cc
            p+=min(4,cnt)*b-r
            if p > m:
                mi = i+1
                m = p
            cnt = max(cnt-4, 0)
            ind = i
        while cnt:
            ind+=1
            p+=min(4,cnt)*b-r
            if p > m:
                mi = ind+1
                m = p
            cnt = max(cnt-4, 0)
        return mi
