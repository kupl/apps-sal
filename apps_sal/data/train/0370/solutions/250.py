class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        # union find
        '''
        def gcd(a, b):    
            if b==0:
                return a
            return gcd(b, a%b)
        '''
        def find(u):  # pass compresson
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

        #pr = []
        # sieve(m-1)
        #l = len(pr)

        p = [-1] * m
        r = [0] * m

        for i in range(n):
            # prime factorization
            factor = 2
            num = A[i]
            while num >= factor * factor:  # here
                if num % factor == 0:
                    num //= factor
                    union(A[i], factor)
                else:
                    factor += 1
            union(A[i], num)    # here

            ################
            #j = 0
            # while j<l and pr[j]<=A[i]:
            #    if A[i]%pr[j]==0:
            #        union(A[i], pr[j])
            #    j+=1
            ##################
            #j = 2
            # while j*j<=A[i]:
            #    if A[i]%j==0:
            #        union(A[i], j)
            #        union(A[i], A[i]//j)
            #    j+=1

        s = [0] * m
        for i in range(n):
            s[find(A[i])] += 1

        return max(s)

        '''
        # dfs   TLE
        
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
