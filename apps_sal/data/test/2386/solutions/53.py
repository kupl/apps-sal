N = int(input())
A = [int(i) for i in input().split()]

def snk(b):
    return sum([abs(A[i]-(b+i+1)) for i in range(N)])
    
l = 1-N
r = 10**9 + N

ans = 10**18

while l+2 < r:
    l1 = (l*2 + r) //3
    r1 = (l + r*2) //3
    ls, rs = [snk(i) for i in [l1, r1]]
    if ls > rs:
      l = l1
    else:
      r = r1
      
ans = 10**18
for i in range(l,r+1):
  ans = min(ans, snk(i))

print(ans) 
