


def __starting_point():
  
  N,K = [int(x) for x in input().split()]
  S = []
  l = [0] * K
  r = [0] * K
  for i in range(K):
    l[i],r[i] = [int(x) for x in input().split()]
  
  dp = [0] * N
  dp[0] = 1
  sdp = [0] * (N+1)
  sdp[0] = 0
  sdp[1] = 1
  for i in range(1,N):

    dp[i] = sum([sdp[max([i-l[k]+1, 0])] - sdp[max([i-r[k], 0])]
                 for k in range(K)]) % 998244353
    sdp[i+1] = (dp[i] + sdp[i]) % 998244353
    

  
    
  print((dp[-1]))

  
  
  




  

  
      


  
    
  
  


__starting_point()
