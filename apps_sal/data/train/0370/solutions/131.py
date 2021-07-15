class Solution:
       def largestComponentSize(self, A):
           def getUniqueDivisors(x:int)->set():
              result = set()
              while x % 2 == 0:
                 result .add(2)
                 x >>= 1
              i = 3
              while i * i <= x:
                 while x % i == 0:
                    result.add(i)
                    x //= i
                 i += 2
              if x > 1:
                 result.add(x)
       
              if x > 1:
                 result.add(x)
              return result
           def findParent(parents:List[int],x:int)->int:
              if parents[x] != x:
                 parents[x]=findParent(parents,parents[x])
              return parents[x]
           n = len(A)
           parents = [i for i in range(n)]
           parentByDivisor = {}
           for i in range(n):
             divisors = getUniqueDivisors(A[i])
             for div in divisors:
                if div in parentByDivisor:
                   root = findParent(parents,parentByDivisor[div])
                   parents[root] = i
                parentByDivisor[div] = i
           counter = [0 for i in range(n)]
           for i in range(n):
              root = findParent(parents,i)
              counter[root] += 1
           return max(counter)
                
           

