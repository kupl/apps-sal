import collections as clc
import math
import time


class UnionFind:
    
    def __init__(self, n: int):
        self.repr = list(range(n))
    
    def find(self, num: int) -> int:
        if num != self.repr[num]:
            self.repr[num] = self.find(self.repr[num])
        return self.repr[num]
    
    def union(self, num1: int, num2: int) -> bool:
        r1 = self.find(num1)
        r2 = self.find(num2)
        if r1 == r2:
            return False
        self.repr[r2] = r1
        return True


class Solution:
    
    def decompose(self, n: int) -> List[int]:
        ans = []
        max_prime = int(math.sqrt(n))
        if n % 2 == 0:
            ans.append(2)
            while n % 2 == 0:
                n //= 2
        prime = 3
        while prime <= max_prime:
            if n % prime == 0:
                ans.append(prime)
                while n % prime == 0:
                    n //= prime
            prime += 2
        if n != 1:
            ans.append(n)
        return ans
    
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        M = max(A)
        node_lists = clc.defaultdict(list)
        for idx, a in enumerate(A):
            for prime in self.decompose(a):
                node_lists[prime].append(idx)
        uf = UnionFind(n)
        for nodes in node_lists.values():
            if len(nodes) <= 1:
                continue
            idx1 = nodes[0]
            for idx2 in nodes[1:]:
                uf.union(idx1, idx2)
        return max(clc.Counter([uf.find(idx) for idx in range(n)]).values())
