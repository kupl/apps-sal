class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
      num1Map = defaultdict(int ) 
      for i,n in enumerate(nums1):
        num1Map[n]+=1
        
      num2Map = defaultdict(int) 
      for i,n in enumerate(nums2):
        num2Map[n]+=1
        
      def count(nums,numsMap):
        out = 0
        same = 0
        for n1 in nums:
          sq = n1 * n1
          for n2,v in list(numsMap.items()):
            if sq/n2 == sq//n2:
              k =numsMap.get(sq//n2)
              if sq//n2 == n2 :
                if k > 1:
                  same+= math.factorial(k)// (math.factorial(k-2) * math.factorial(2)  )
              elif k:
                out+= k * v
        return same +out//2 
      
      out=0   
      out +=count(nums1,num2Map)     
      out +=count(nums2,num1Map)     
      return out 
      
      

