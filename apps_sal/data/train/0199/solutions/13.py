class Solution:
     def longestConsecutive(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         def union(uf, p, q):
             i, j = root(uf, p), root(uf, q)
             uf[i], uf[j] = min(i, j), min(i, j)
         def root (uf, p):
             while p != uf[p]:
                 uf[p] = uf[uf[p]]
                 p = uf[p]
             return p
         if len(nums) == 0:
             return 0
         ht = {}
         uf = [i for i in range(len(nums))]
         for i, n in enumerate(nums):
             if n not in ht:
                 ht[n] = i
             else:
                 continue
             m, o = n - 1, n + 1
             if m in ht:
                 union(uf, ht[m], i)
             if o in ht:
                 union(uf, ht[o], i)
         roots = {}
         for x in uf:
             r = root(uf, x)
             if r in roots:
                 roots[r] += 1
             else:
                 roots[r] = 1
         return max(roots.values())

