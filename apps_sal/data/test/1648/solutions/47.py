from scipy.special import comb
n = 1000000007
 
a,b = map(int, input().split())
 
for i in range(1,b+1):
  print(comb(a-b+1, i, exact=True)*comb(b-1, i-1, exact=True)%n)
