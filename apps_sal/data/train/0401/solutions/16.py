




class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        res = 0
        total = sum(nums)
        
        #only consider removing numbers that are not already divisible by 3
        remove = tuple(sorted(n for n in nums if n%3))
        
        q = collections.deque([(total, 0)]) #total and bitmasked removed numbers
        visited = set([0])
        
        while q:
            
            t, r = q.popleft()
            
            if not t%3:
                res = max(res, t)
                continue

            if t <= res:
                continue

            for i in range(len(remove)):
                if not (1 << i) & r:
                    b = (1 << i) | r
                    if b not in visited:
                        visited.add(b)
                        q.append((t-remove[i], b))
        
        return res
