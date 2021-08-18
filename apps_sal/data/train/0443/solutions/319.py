class Solution:
    def choose_inc(self, idx, num, gt, stack):
        if num == 0:
            self.soln.add(tuple(stack))
            return
        for jidx in range(idx, len(self.rating)):
            jnum = self.rating[jidx]
            if jnum > gt:
                self.choose_inc(jidx + 1, num - 1, jnum, stack + [jnum])

    def numTeams(self, rating: List[int]) -> int:
        self.soln = set()
        self.rating = rating
        self.choose_inc(0, 3, 0, [])
        sol_fwd = list(self.soln)
        self.soln = set()
        self.rating.reverse()
        self.choose_inc(0, 3, 0, [])
        return len(sol_fwd) + len(self.soln)
