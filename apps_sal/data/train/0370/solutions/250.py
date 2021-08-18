class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        '''
        def gcd(a, b):    
            if b==0:
                return a
            return gcd(b, a%b)
        '''
        def find(u):
            if p[u] == -1:
                return u
            p[u] = find(p[u])
            return p[u]

        def union(u, v):
            u = find(u)
            v = find(v)

            if u != v:
                if r[u] > r[v]:
                    p[v] = u
                elif r[u] < r[v]:
                    p[u] = v
                else:
                    p[v] = u
                    r[u] += 1
        '''
        def sieve(x):
            
            num = [True]*(x+1)
            
            k = 2
            while k*k<=x:
                if num[k]:
                    i = k*k
                    while i<=x:
                        num[i] = False
                        i += k
                k+=1        
                
            for i in range(2, x+1):
                if num[i]:
                    pr.append(i)
            
        '''
        n = len(A)

        m = max(A) + 1

        p = [-1] * m
        r = [0] * m

        for i in range(n):
            factor = 2
            num = A[i]
            while num >= factor * factor:
                if num % factor == 0:
                    num //= factor
                    union(A[i], factor)
                else:
                    factor += 1
            union(A[i], num)

        s = [0] * m
        for i in range(n):
            s[find(A[i])] += 1

        return max(s)

        '''
        
        def gcd(a, b):    
            if b==0:
                return a
            return gcd(b, a%b)
        
        def dfs(u):
            y = 1
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    y += dfs(v)
            
            return y
        
        
        n = len(A)
        
        adj = [ [] for i in range(n) ]
        
        for i in range(n):
            for j in range(i+1,n):
                if gcd(A[i], A[j])>1:
                    adj[i].append(j)
                    adj[j].append(i)
        
        
        
        res = 0
        
        vis = [False]*n
        
        for i in range(n):
            
            if not vis[i]:
                vis[i] = True
                res = max(res, dfs(i))
        
        return res
    '''
