class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
      
      pre = [True]
      pst = [True]
      for i in range(1, len(arr)):
        if pre[-1] and arr[i]>=arr[i-1]:
          pre.append(True)
        else: pre.append(False)
        
        if pst[-1] and arr[len(arr)-i-1]<=arr[len(arr)-i]:
          pst.append(True)
        else: pst.append(False)
      
      
      pst = pst[::-1]
      # print (pre)
      # print (pst)
      
      def isPoss(slen):
        for i in range(len(arr)-slen+1):
          j = i+slen
          
          if not i:
            if pst[j]: return True
          elif j>len(arr)-1:
            if pre[i-1]: return True
          else:
            if pre[i-1] and pst[j] and arr[i-1]<=arr[j]:
              return True
          
        return False
            
      # print (isPoss(1))
      l, r = 0, len(arr)
      res = r
      while l<=r:
        m = l + (r-l)//2
        if isPoss(m):
          res = min(m, res)
          r = m - 1
        else:
          l = m + 1
      return res
