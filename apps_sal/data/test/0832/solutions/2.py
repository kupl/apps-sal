import sys
inp = sys.stdin
n = int(inp.readline())
H = []
A = []
for i in range(n):
  h,a = inp.readline().split()
  H.append(h)
  A.append(a)
ans = 0  
for i in range(n):
  for j in range(n):    
    if i != j and H[i] == A[j]:
      ans += 1  
print(ans)  
