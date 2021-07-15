class Solution:
    def minOperationsMaxProfit(self, a: List[int], bc: int, rc: int) -> int:
        ans, cnt = 0, 0
        w = 0
        m = []
        for x in a:
            x = x + w
            # if x > 0:
            ans += min(x, 4) * bc - rc
            cnt += 1
            m.append((ans, cnt))
            w = max(x - 4, 0)
        while w > 0:
            ans += min(w, 4) * bc - rc
            cnt += 1
            m.append((ans, cnt))
            w = max(w - 4, 0) 
            
        res = max(m, key=lambda x: (x[0], -x[1]))
        # print(m)
        # print(res)
        return res[1] if res[0] > 0 else -1
