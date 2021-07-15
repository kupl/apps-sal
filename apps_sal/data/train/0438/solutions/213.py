# class Solution:
#     def findLatestStep(self, arr: List[int], m: int) -> int:
#         n = len(arr)
#         if n == m:
#             return n
#         temp = [1]*n
#         j = n
#         while j > 0:
#             temp[arr[j-1]-1] = 0
#             count = 0
#             for i, y in enumerate(temp):
#                 if y == 1:
#                     count += 1
#                 else:
#                     count = 0
#                 if count == m and (i+1 >= n or (i+1 < n and temp[i+1] == 0)):
#                     return j - 1
#             j -= 1
#         return -1

# class Solution:
#     def findLatestStep(self, A, m):
#         if m == len(A): return m
#         length = [0] * (len(A) + 2)
#         res = -1
#         for i, a in enumerate(A):
#             left, right = length[a - 1], length[a + 1]
#             if left == m or right == m:
#                 res = i
#             length[a - left] = length[a + right] = left + right + 1
#         return res

class UnionFindSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        
    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
            self.ranks[pu] += self.ranks[pv]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        return True

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        
        n, ans = len(arr), -1
        uf = UnionFindSet(n)
        
        for step, i in enumerate(arr):
            i -= 1
            uf.ranks[i] = 1
            for j in (i - 1, i + 1):
                if 0 <= j < n:
                    if uf.ranks[uf.find(j)] == m:
                        ans = step
                    if uf.ranks[j]:
                        uf.union(i, j)
        
        return ans
        

