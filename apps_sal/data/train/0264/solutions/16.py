class Solution:

    def maxLength(self, arr: List[str]) -> int:
        self.out = set()
        self.visited = set()
        opts = []
        for sub in arr:
            tmp = set()
            omit = False
            for ch in sub:
                if ch in tmp:
                    omit = True
                tmp.add(ch)
            if not omit:
                opts.append(tmp)
        self.dfs(set(), opts)
        return len(self.out)

    def dfs(self, curr, opts):
        if tuple(sorted(curr)) in self.visited:
            return
        self.visited.add(tuple(sorted(curr)))
        if len(curr) > len(self.out):
            self.out = curr
        if not opts:
            return
        for (j, opt) in enumerate(opts):
            if not curr.intersection(opt):
                self.dfs(curr.union(opt), opts[:j] + opts[j + 1:])
