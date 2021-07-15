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

# def main():
  

# # main()
# print(main())

n,a,b,c=LI()
l=[I() for _ in range(n)]
answer=inf

def f(lst,ind):
  nonlocal answer
  if ind==n:
    ac=lst.count(1)
    bc=lst.count(2)
    cc=lst.count(3)

    if ac==0 or bc==0 or cc==0:
      return min(answer,inf)

    _a=_b=_c=0
    for i,x in enumerate(lst):
      if x==1:
        _a+=l[i]
      elif x==2:
        _b+=l[i]
      elif x==3:
        _c+=l[i]
    # 合わなかった原因。短縮できることを忘れてた
    # if _a>a or _b>b or _c>c:
    #   return min(answer,inf)

    sm=0
    sm+=max(0,ac-1)*10
    sm+=max(0,bc-1)*10
    sm+=max(0,cc-1)*10
    sm+=abs(a-_a)
    sm+=abs(b-_b)
    sm+=abs(c-_c)

    return min(answer,sm)

  else:
    for i in range(4):
      lst[ind]=i
      answer=min(answer,f(lst,ind+1))

  return answer

lst=[-1]*n
print((f(lst,0)))

