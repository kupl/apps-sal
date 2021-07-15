class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        mp={} # for union find
        ans=0
        
        def find(a):
            if a not in mp: mp[a]=a
            if mp[a]!=a:
                mp[a]=find(mp[a])
            return mp[a]
            
        def union(a,b): # b is smaller
            pa=find(a)
            pb=find(b)
            if pa!=pb:
                mp[pa]=pb
            
        for a in A:
            for factor in self.primes_set(a):
                union(a,factor)
        return collections.Counter([find(a) for a in A]).most_common(1)[0][1]
    
    def primes_set(self,n): # much fast using this primes set
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])                
