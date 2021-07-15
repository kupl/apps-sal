# https://leetcode.com/problems/find-latest-group-of-size-m/discuss/806718/Python-Clean-Union-Find-solution-with-explanation-O(N)
# This solution utilize union by rank with 2 aims: count number of one as well as reduce the TC. One main point is that last step of group of ones of length m means we need bit set to ruin the last group of ones with length of m, or the this type of group will last until last step, so we can determine the result by determining the rank of left and right of currrent bit set. After one pass of arr, we can check if ranks of our union equal m.
class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, src: int) -> int:
        if self.parents[src] == src:
            return src
        self.parents[src] = self.find(self.parents[src])
        return self.parents[src]
    
    def union(self, src: int, dest: int) -> bool:
        rootSrc, rootDest = self.find(src), self.find(dest)
        if rootDest == rootSrc:
            return False
        
        if self.ranks[rootSrc] > self.ranks[rootDest]:
            self.parents[rootDest] = rootSrc
            self.ranks[rootSrc] += self.ranks[rootDest]
        else:
            self.parents[rootSrc] = rootDest
            self.ranks[rootDest] += self.ranks[rootSrc]
        return True
    
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n, result = len(arr), -1
        uf = UnionFind(n)

        for step, idx in enumerate(arr):
            idx -= 1
            uf.ranks[idx] = 1
            for j in (idx - 1, idx + 1):
                if 0 <= j < n:
                    if uf.ranks[uf.find(j)] == m:
                        result = step
                    if uf.ranks[j]:
                        uf.union(idx, j)

        for i in range(n):
            if uf.ranks[uf.find(i)] == m:
                return n
        return result
