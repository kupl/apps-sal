class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        '''
        def computeGCD(x,y):
            while(y):
                x,y=y,x%y
            return x

        res=collections.defaultdict()
        A=sorted(A)
        for i in A:
            temp=[]
            tem=A.copy()
            tem.remove(i)
            for j in tem:
                if computeGCD(i,j)>1:
                    temp.append(j)

            res[i]=temp
        final=[]
        def dfs(i, visited):
            if res[i]==[]:
                return 1

            temp=[]
            for j in res[i]:
                if visited[A.index(j)]==False:
                    visited[A.index(j)]=True
                    t=dfs(j,visited)
                    temp.append(1+t)
            print(i,res[i],temp)
            if temp:
                return max(temp)
            return 1
        for i in res:
            visited=[False]*len(A)
            visited[A.index(i)]=True
            final.append(dfs(i, visited))
        print(final,res)
        return max(final)
        '''
        parent = {}

        def ufind(a):
            if a not in parent:
                parent[a] = a
            if a != parent[a]:
                parent[a] = ufind(parent[a])
            return parent[a]

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)

            parent[ua] = ub

        count = collections.Counter()
        for x in A:
            factors = []
            y = 2
            while x >= y * y:
                if x % y == 0:
                    factors.append(y)
                    while x % y == 0:
                        x //= y
                y += 1
            if x > 1:
                factors.append(x)

            for a, b in zip(factors, factors[1:]):
                uunion(a, b)

            if len(factors) > 0:
                count[factors[0]] += 1

        final_count = collections.Counter()
        for key in list(count.keys()):
            final_count[ufind(key)] += count[key]

        best = 0
        for key in list(final_count.keys()):
            best = max(best, final_count[key])

        return best
