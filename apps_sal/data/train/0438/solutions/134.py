class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        parents = [i for i in range(N + 1)]
        sizes = [1 for i in range(N + 1)]
        
        def ufind(a):
            if parents[a] == a:
                return a
            parents[a] = ufind(parents[a])
            return parents[a]
        
        def uunion(a, b):
            ra = ufind(a)
            rb = ufind(b)
            if ra != rb:
                parents[rb] = parents[ra]
                sizes[ra] += sizes[rb]
                
        def usize(a):
            return sizes[ufind(a)]
        
        ans = -1
        seen = set()
        counter = collections.defaultdict(int)
        
        for i, x in enumerate(arr):
            lft = 0
            if x - 1 > 0 and (x - 1) in seen:
                lft = usize(x - 1)
                counter[lft] -= 1
                uunion(x, x - 1)
                
            rgt = 0
            if x + 1 <= N and (x + 1) in seen:
                rgt = usize(x + 1)
                counter[rgt] -= 1
                uunion(x, x + 1)
                
            grp = lft + 1 + rgt
            counter[grp] += 1
            
            if counter[m] > 0:
                ans = max(ans, i + 1)
                
            seen.add(x)
                
        return ans
