from collections import Counter, defaultdict


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def factorize(x):
            ret = set()
            i = 2
            while i * i <= x:
                while x % i == 0:
                    ret.add(i)
                    x = x // i
                i += 1
            
            if x != 1:
                ret.add(x)
            return ret
        
        factor_to_num = defaultdict(list)
        for i, a in enumerate(A):
            for factor in factorize(a):
                factor_to_num[factor].append(i)
        
        # init
        par = list(range(len(A)))
        rank = [0] * len(A)
        
        def find(x):
            if par[x] == x:
                return x
            else:
                ret = find(par[x])
                par[x] = ret
                return ret
        
        def unite(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            
            if rank[x] < rank[y]:
                par[x] = y
            else:
                par[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        for factor in factor_to_num.keys():
            nums = factor_to_num[factor]
            for i in range(1, len(nums)):
                unite(nums[i-1], nums[i])
        
        counter = Counter(find(i) for i in range(len(A)))
        return max(counter.values())
