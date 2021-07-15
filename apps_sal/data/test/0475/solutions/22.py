
mod=998244353
def nCrModp(n, r): 
  
    # The array C is going to store last row of 
    # pascal triangle at the end. And last entry 
    # of last row is nCr. 
    C = [0 for i in range(r+1)] 
  
    C[0] = 1 # Top row of Pascal Triangle 
  
    # One by constructs remaining rows of Pascal 
    # Triangle from top to bottom 
    for i in range(1, n+1): 
  
        # Fill entries of current row  
        # using previous row values 
        for j in range(min(i, r), 0, -1): 
  
            # nCj = (n - 1)Cj + (n - 1)C(j - 1) 
            C[j] = (C[j] + C[j-1]) % mod
  
    return C[r]

n,m,k=map(int,input().split())
if(m==1 and k>0):
    print(0)
else:
    ans=m
    ans=((ans%mod)*(pow(m-1,k,mod)%mod))%mod
    val1=nCrModp(n-1,k)
    ans=((ans%mod)*(val1%mod))%mod
    print(ans)
