class Solution:
    def minDays(self, b: List[int], m: int, k: int) -> int:
        mi, ma = min(b), max(b)
        if m * k > len(b):
            return -1
        n = len(b)
        cur, adj = 0, 0
        while(mi < ma):
            mid = (mi + ma) // 2
            cur, adj = 0, 0
            for i in range(n):
                if(mid < b[i]):
                    adj = 0
                else:
                    adj += 1
                    if(adj == k):
                        cur += 1
                        adj = 0
                if(cur >= m):
                    break
            if(cur < m):
                mi = mid + 1
            else:
                ma = mid
        return mi
