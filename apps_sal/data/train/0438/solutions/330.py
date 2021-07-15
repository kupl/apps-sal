# class Solution(object):
#     def findLatestStep(self, arr, m):
#         \"\"\"
#         :type arr: List[int]
#         :type m: int
#         :rtype: int
#         \"\"\"
#         self.rank = collections.defaultdict(int)
#         self.p = collections.defaultdict(int)
        
#         def find(i):
#             if i not in self.p:
#                 self.p[i] = i
#                 self.rank[i] = 1
#                 return i
#             p = self.p[i]
#             while p != self.p[p]:
#                 p = self.p[p]
#             self.p[i] = p
#             return p
        
#         def union(i, j):
#             ip, jp = find(i), find(j)
#             if ip == jp:
#                 return False
#             ir, jr = self.rank[ip], self.rank[jp]
#             if ir > jr:
#                 self.p[jp] = ip
#                 self.rank[ip] += self.rank[jp]
#                 self.rank.pop(jp)
#             else:
#                 self.p[ip] = jp
#                 self.rank[jp] += self.rank[ip]
#             return True
        
        
#         status = [0] * len(arr)
#         res = -1
#         l = len(arr)
#         for step, i in enumerate(arr):
#             i -= 1
#             status[i] = 1
#             self.p[i] = i
#             self.rank[i] = 1
#             for j in [i-1, i+1]:
#                 if 0<= j < l:
#                     if self.rank[find(j)] == m:
#                         res = step
#                         print(self.p)
#                         print(self.rank)
#                     if status[j] == 1:
#                         union(i, j)
                        
#         for i in range(l):
#             if self.rank[find(i)] == m:
#                 return l
            
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
        elif self.ranks[pv] > self.ranks[pu]:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        else:
            self.parents[pu] = pv
            self.ranks[pv] += self.ranks[pu]
        return True

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
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
        
        for i in range(n):
            if uf.ranks[uf.find(i)] == m:
                return n
            
        return ans
