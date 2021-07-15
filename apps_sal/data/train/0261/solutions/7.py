class Solution:
     def swap(self, A, i, j ):
         if A[i] != A[j]:
             A[i],A[j] = A[j],A[i]
     def partition(self, A, p, r):
         self.swap(A, r, random.randint(p, r))
         x = A[r]
         j = p - 1
         for i in range(p, r):
             if A[i] <= x:
                 j += 1
                 self.swap(A, i, j)
         j += 1
         self.swap(A, r, j)
         return j
     def findElement(self, A, k):
         low, high = 0, len(A) - 1
         while low < high:
             i = self.partition(A, low, high)
             if i > k:
                 high = i - 1
             elif i < k :
                 low = i + 1
             else:
                 return A[k]
         return A[k]
     
     def findKthLargest(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: int
         """
         return self.findElement(nums, len(nums) - k)

