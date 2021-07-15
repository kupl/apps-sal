from collections import defaultdict

class Solution:
    def helper(self, x):
            if x == 2:
                return 1
            if x in self.table:
                return self.table[x]
            if x % 2:
                y = int(3*x+1)
            else:
                y = int(x/2)
            ans = 1+self.helper(y)
            if self.lo <= x <= self.hi:
                self.table[x] = ans
            return ans
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.table = dict()
        self.lo = lo
        self.hi = hi
        powers = [self.helper(x) for x in range(lo, hi+1)]
        tosort = list(zip(powers, list(range(lo, hi+1))))
        return sorted(tosort)[k-1][1]
        # print(ranks)
    
        # doesnt work
        # todo = set(range(lo, hi+1))
        # if len(todo) == 1:
        #     return 1
        # ranks = []
        # while todo:
        #     y = todo.pop()
        #     stack = [y]
        #     while y > 1 and y not in table:
        #         if y % 2:
        #             y = 3*y+1
        #         else:
        #             y = y/2
        #         if y in todo:
        #             todo.remove(y)
        #         stack.append(y)
        #     if y == 1:
        #         ranks = ranks + stack
        #     else:
        #         for i in range(len(stack)-1):
        #             ranks.insert(ranks.index(stack[-i])+1, stack[-i-1])
        # i = 0
        # nums = set(range(lo, hi+1))
        # for r in reversed(ranks):
        #     if r in nums:
        #         i += 1
        #         print(r)
        #     if i == k:
        #         return int(r)

