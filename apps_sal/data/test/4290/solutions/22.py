from scipy.special import comb
N,M = input().split()
N = int(N)
M = int(M)

A = 0
B = 0
if N >= 2 :
  A = comb(N, 2, exact=True)

if M >= 2 :
  B = comb(M, 2, exact=True)
 
print(A + B)
