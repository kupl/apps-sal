class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
    
        def memo(f):
            dic = {}
            def f_alt(*args):
                if args not in dic:
                    dic[args] = f(*args)
                return dic[args]
            return f_alt

        key = lambda s: (len(s),s)
        
        cands = {}
        for i,c in enumerate(cost):
            cands[c]=i+1
        
        @memo
        def f(tar):
            if tar == 0:
                return 0
            if tar>0:
                ans = 0
                for c in cands:
                    if f(tar-c) != None:
                        ans = max(ans, 10*f(tar-c) + cands[c])
                return ans or None
        
        return str(f(target) or 0)

