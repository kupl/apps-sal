class Solution1:
    def largestComponentSize(self, A):
        if not A: return 0
        def findAndCompact(l, i): # require i >= 0
            if l[i] == i: return i
            p = l[i]
            if p >= 0 and l[p] == p: return p
            while p >= 0 and l[p] != p:
                p = l[p]
            root = p
            
            # compact
            p = i
            while p >= 0 and l[p] != p:
                t = l[p]
                l[p] = root
                p = t
            return root
        
        slist = [-1] * len(A)
        d = {} # record prime->(root of union-find set)
        for i in range(len(A)):
            n = A[i]
            has_factor = False
            for j in range(2, int(sqrt(n)) + 1):
                if n % j == 0:
                    has_factor = True
                    k = n // j
                    #print(n, j, k)
                    ri = -1 if slist[i] < 0 else findAndCompact(slist, slist[i])
                    rj = -1 if j not in d else findAndCompact(slist, d[j])
                    rk = -1 if k not in d else findAndCompact(slist, d[k])
                    if ri < 0 and rj < 0 and rk < 0:
                        slist[i] = d[j] = d[k] = i
                    else:
                        mm = min([item for item in (ri, rj, rk) if item >= 0])
                        if slist[i] >= 0: slist[ri] = mm
                        if j in d: slist[rj] = mm
                        if k in d: slist[rk] = mm
                        slist[i] = d[j] = d[k] = mm
            if not has_factor: #prime
                if A[i] not in d: slist[i] = d[A[i]] = i
                else: slist[i] = d[A[i]]
            #print(slist, d)
        
        for i in range(len(A)): findAndCompact(slist, i)
        #print('### ', slist)
        cc = Counter(slist)
        m = cc.most_common(2)
        return m[0][1] if m[0][0] != -1 else m[1][1]
    
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        n = self.p[x]
        while n >= 0 and self.p[n] != n:
            n = self.p[n]
        root = n
        # compact
        n = x
        while n >= 0 and self.p[n] != n:
            t = self.p[n]
            self.p[n] = root
            n= t
        return root

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr

class Solution:
    def primes_set(self,n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])

    def largestComponentSize(self, A):
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set: primes[q].append(i)

        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                UF.union(UF.find(indexes[i]), UF.find(indexes[i+1]))

        return max(Counter([UF.find(i) for i in range(n)]).values())
