class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        self.min_cost = min(cost)
        self.cost = cost
        self.mem = dict()
        rv = self.dfs(target)
        if rv is None:
            return '0'
        return rv
        
    def dfs(self, target):
        if target == 0:
            return ''
        elif target < self.min_cost:
            return None
        
        key = (target)
        if key in self.mem:
            return self.mem[key]
        
        res = ''
        for i, c in enumerate(self.cost):
            rv = self.dfs(target - c)
            if rv != None:
                res = self.get_max(res, str(i+1) + rv)

        if res == '':
            res = None
        self.mem[key] = res
        return res
            
            
            
    def get_max(self, s1, s2):
        if len(s1) != len(s2):
            if len(s1) > len(s2):
                return s1
            return s2
        if s1 > s2:
            return s1
        return s2
