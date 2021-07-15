import math
 
n,k = map(int, input().split())
 
def main(i):
  blue = math.factorial(k-1) // (math.factorial(i-1) * math.factorial(k-i))
  red = math.factorial(n-k+1) // (math.factorial(n-k+1-i) * math.factorial(i))
  print((blue*red) % (10**9 + 7))
 
for i in range(1, k+1):
  if i > n-k+1:
    print('0')
  else:
   main(i)
