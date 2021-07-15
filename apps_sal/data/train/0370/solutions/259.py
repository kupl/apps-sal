class UnionFind:
    def __init__(self, nums):
        self.nums = nums
        self.groups = list(range(len(nums)))
        self.sizes = [1] * len(nums)
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        
        if self.sizes[a] < self.sizes[b]:
            a, b = b, a

        self.sizes[a] += self.sizes[b]
        self.groups[b] = self.groups[a]

    def find(self, a):
        head = self.groups[a]
        while head != self.groups[head]:
            head = self.groups[head]

        node = self.groups[a]
        while node != self.groups[node]:
            node, self.groups[node] = self.groups[node], head

        return head

    def largest(self):
        return max(self.sizes)

class Solution:
    def largestComponentSize(self, a: List[int]) -> int:
        def factors(n):
            ans = {n}
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    ans.add(i)
                    ans.add(n // i)
            return ans
        
        uf = UnionFind(a)
        primes = defaultdict(list)
        for i, num in enumerate(a):
            pr_set = factors(num)
            for prime in pr_set:
                primes[prime].append(i)
        
        for prime, idxs in primes.items():
            for i in range(len(idxs) - 1):
                uf.union(idxs[i],idxs[i + 1])
        return uf.largest()
