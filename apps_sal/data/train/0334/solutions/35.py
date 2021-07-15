class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        rlist = []
        cnt = 0
        for i in range(1, len(s)):
            c = s[i]
            if c == s[i-1]:
                cnt += 1
            else:
                if cnt > 0:
                    rlist.append([i-cnt-1, i])
                cnt = 0
            if i == len(s)-1 and cnt > 0:
                rlist.append([i-cnt, i+1])
        ans = []
        for r in rlist:
            if r[1]-r[0] > 1:
                t = sorted(cost[r[0]:r[1]])
                ans.append(sum(t[:-1]))
            else:
                ans.append(min(cost[r[0]:r[1]]))
        return sum(ans)
