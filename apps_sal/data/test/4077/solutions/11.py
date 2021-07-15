class BinaryIndexedTree:
  def __init__(self, n):
    self.bit = [0] * n

  def add(self, i, x):
    i += 1
    while i <= len(self.bit):
      self.bit[i-1] += x
      i += i & -i

  def sum_sub(self, i):
    a = 0
    i += 1
    while i:
      a += self.bit[i-1]
      i -= i & -i
    return a

  def sum(self, i, j):
    a = 0
    if j != 0:
      a += self.sum_sub(j-1)
    if i != 0:
      a -= self.sum_sub(i-1)
    return a

def f(m):
  ans=0
  bit=BinaryIndexedTree(2*n+7)
  f=0
  for i in range(n):
    bit.add(n+f,1)
    if a[i]>m:f-=1
    else:f+=1
    ans+=bit.sum_sub(n+f)
  return ans
n,m=map(int,input().split())
a=list(map(int,input().split()))
print(f(m)-f(m-1))
