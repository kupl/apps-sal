def div(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def main():
  import functools
  import operator
  import numpy as np
  import itertools
  import math
  lis = [1]
  N = int(input())
  x = div(N)
  A = []
  for i in range(math.ceil(len(x)/2)):
    A.append(x[i]+x[len(x)-i-1])
  ans = min(A)-2
  print(ans)
main()
