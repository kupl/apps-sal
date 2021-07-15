class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        n = len(arr)
        
        rank = [0 for i in range(n + 1)]
        fa  =  [i for i in range(n + 1)]
        def getfa(x):
            if fa[x] == x: return x
            fa[x] = getfa(fa[x])
            return fa[x]
        
        def union(a, b):
            p, q = getfa(a), getfa(b)
            if p != q:
                if rank[p] >= rank[q]:
                    fa[q] = p
                    rank[p] += rank[q]
                    return p
                else:
                    fa[p] = q
                    rank[q] += rank[p]
                    return q
                
            return False
        
        cc = Counter()
        last = -1
        for i, num in enumerate(arr):
            l, r = num - 1, num + 1
            rank[num] = 1
            cc[1] += 1
            if rank[l]:
                rl = getfa(l)
                cc[1] -= 1
                cc[rank[rl]] -= 1
                newroot = union(num, rl)
                cc[rank[newroot]] += 1
            if r <= n and rank[r]:
                rl = getfa(num)
                cc[rank[rl]] -= 1
                rr = getfa(r)
                cc[rank[rr]] -= 1
                newroot = union(rl, rr)
                cc[rank[newroot]] += 1
            if cc[m] > 0:
                last = i + 1
                
        return last
                
                
                

