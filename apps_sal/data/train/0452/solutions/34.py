class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jD=jobDifficulty
        day=d
        self.memo = {}
        def dp(i,day):
            if (i,day) not in self.memo:
                if i < day: self.memo[(i,day)] = float('inf')
                elif day == 1: self.memo[(i,day)] = max(jD[:i])
                elif i == day: self.memo[(i,day)] = sum(jD[:i])
                else:
                    tmp = jD[i-1]
                    self.memo[(i,day)] = dp(i-1,day-1) + tmp
                    for j in range(i-1,day-3,-1):
                        tmp = max(jD[j-1],tmp)
                        self.memo[(i,day)] = min(self.memo[(i,day)],dp(j,day-1) + tmp)
            return self.memo[(i,day)]
        ans = dp(len(jD),d)
        return ans if ans!= float('inf') else -1

