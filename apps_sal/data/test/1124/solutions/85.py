n = int( input())
a = list( map( int, input().split()))
import functools
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)
def gcd(nums):
  return functools.reduce(euclid, nums)
print(gcd(a))
