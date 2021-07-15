import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Summarize count of factor within list -- START --
def summarizeList(l):
  sl=sorted(l)

  a=sl[0]
  c=1
  res=[]

  for x in sl[1:]:
    if x==a:
      c+=1
    else:
      res.append([a,c])
      a=x
      c=1
  res.append([a,c])

  return res
# Summarize count of factor within list --- END ---

# 累積和の書き方がよくないやつ
def main():
  s=S()
  n=len(s)

  l=[]
  mul=1
  for x in s[::-1]:
    l.append(mul*int(x)%2019)
    mul*=10
    mul%=2019

  for i in range(n-1):
    l[i+1]+=l[i]
    l[i+1]%=2019

  sl=summarizeList(l)
  # print(sl)

  ans=0
  for x,c in sl:
    if x==0:
      ans+=c
    if c>1:
      ans+=c*(c-1)//2

  return ans

# main()
print((main()))

