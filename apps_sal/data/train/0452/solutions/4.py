class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        self.memo = {}
        self.mxs = []
        mx = 0
        for j in jobDifficulty:
            mx = max(mx, j)
            self.mxs.append(mx)
        return self.recurse(jobDifficulty, len(jobDifficulty) - 1, d)
        
    def recurse(self, jd, start, remain):
        # if start == 0:
        #     return jd[0]
        if remain == 1:
            # return max(jd[:start + 1])
            return self.mxs[start]
        
        if (start, remain) in self.memo:
            return self.memo[(start, remain)]
        
        mx = 0
        mn = float('inf')
        
        for j in range(start, 0, -1):
            curr = jd[j]
            mx = max(mx, curr)
            mn = min(mn, mx + self.recurse(jd, j - 1, remain - 1))
        self.memo[(start, remain)] = mn
        # print((start, remain), self.memo, mx, mn)
        return mn
