class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        DP=[0]*len(arr)
        N=len(arr)
        DP[0]=arr[0]
        m=arr[0]
        for i in range(k):
            m=max(m,arr[i])
            DP[i]=m*(i+1)
            
      #  print(DP)
        for i in range(k,N):
            mm=arr[i]
            DP[i]=DP[i-1]+arr[i]
        #    print(DP[i],i)
          #  print(i,DP,mm,arr[i])
            for j in range(1,k):
                mm=max(mm,arr[i-j])
             #   print(i,mm,arr[i-j],DP[i-j])
                DP[i]=max(DP[i],DP[i-j-1]+mm*(j+1))
            #DP[i]=max(DP[i-1]+arr)
    #    print(DP)
        return DP[-1]
  #  [5,7,7,7,7]

