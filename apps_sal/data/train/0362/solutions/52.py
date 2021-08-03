class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        self.hat_to_man = collections.defaultdict(set)
        for i, lt in enumerate(hats):
            for hat in lt:
                self.hat_to_man[hat].add(i)

        self.hat_nums = sorted(self.hat_to_man)
        self.hat_cnt = len(self.hat_nums)
        self.man_cnt = len(hats)
        self.mem = dict()

        return self.dfs(0, set())

    def dfs(self, idx, used):
        if idx >= self.hat_cnt:
            return 0

        key = (idx, frozenset(used))
        if key in self.mem:
            return self.mem[key]

        hat = self.hat_nums[idx]
        res = 0
        for x in self.hat_to_man[hat] - used:
            used.add(x)
            if len(used) == self.man_cnt:
                res += 1
                used.remove(x)
                continue
            res += self.dfs(idx + 1, used)
            used.remove(x)

        res += self.dfs(idx + 1, used)

        self.mem[key] = res
        return res % (10**9 + 7)
