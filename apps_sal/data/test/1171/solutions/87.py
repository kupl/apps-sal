N,K = list(map(int,input().split()))
V = list(map(int,input().split()))
#print(V)
max_v = 0
have_minus = []
for left in range(N):
  for right in range(left,N + 1)[::-1]:
    if len(V[:left]) + len(V[right:]) > K: 
      break
    #print (V[:left], V[right:])
    sum_ = sum(V[:left]) + sum(V[right:])
    have_minus = [num for num in V[:left]+V[right:] if num < 0]
    have_minus.sort()
    #print (f"have_minus={have_minus}" )
    d = max(0,K - (len(V[:left]) + len(V[right:])))
    for i in range(min(d, len(have_minus))):
        sum_ -= have_minus[i]   
    #print (f"sum_ = {sum_}")    
    
    max_v = max(max_v ,sum_)
print(max_v)      
    
    
       

