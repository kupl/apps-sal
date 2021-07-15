class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        A = sorted(A)
        
        def factors(a):
            fact = set()
            for i in range(2, math.isqrt(a)+1):
                if a%i ==0:
                    fact.add(i)
                    fact.add(a//i)
            fact.add(a)
            return fact

        
        parent = [i for i in range(len(A))]
        nodes = [1] * len(A)
        rank = [1] * len(A)
        
        def find(a):
            if parent[a] == a:
                return a
            parent[a] = find(parent[a])
            return parent[a]
        
        def union(a,b):
            pa, pb = find(a), find(b)
            if rank[pa] >pb:
                parent[pb] = pa
                nodes[pa] += nodes[pb]
            elif rank[pa] >pb:
                parent[pa] = pb
                nodes[pb] += nodes[pa]
            else:
                parent[pb] = pa
                nodes[pa] += nodes[pb]
                rank[pa] +=1
        
        m = {}
        
        for i in range(len(A)):
            facts = factors(A[i])
            for f in facts:
                if f in m and find(i)  != find(m[f]):
                    union(i, m[f])
                else:
                    m[f] = i
            
                    
            
                    
        return max(nodes)
                    
                
                

