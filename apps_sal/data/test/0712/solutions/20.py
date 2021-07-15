n, p, t = list(map(float, input().split()))
n, t = int(n + 0.5), int(t + 0.5)
if p < 0.001 or p > 0.999: 
  print(n * p)
  return
from math import exp, lgamma, log
print('%.10f' %sum( exp(i * log(p) + (t - i) * log(1 - p) + lgamma(t + 1) - lgamma(i + 1) - lgamma(t - i + 1)) * min(i, n) for i in range(t + 1))) 

