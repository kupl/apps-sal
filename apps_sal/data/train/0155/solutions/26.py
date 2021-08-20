class Solution:

    def maxJumps(self, arr: List[int], d: int) -> int:
        l = len(arr)
        (self.check, self.seen) = ([[] for _ in range(l)], dict())
        for (i, v) in enumerate(arr):
            for sign in (1, -1):
                for x in range(sign, (d + 1) * sign, sign):
                    if i + x not in list(range(l)) or v <= arr[i + x]:
                        break
                    self.check[i].append(i + x)
            if not self.check[i]:
                self.seen[i] = 1
        return max((self.helper(i) for i in range(l)))

    def helper(self, p):
        if p not in self.seen:
            res = 0
            for n in self.check[p]:
                res = max(res, self.seen.get(n, self.helper(n)) + 1)
            self.seen[p] = res
        return self.seen[p]
