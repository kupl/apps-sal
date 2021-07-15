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

def main():
  h,w,d=LI()
  l=[LI() for _ in range(h)]

  q=I()
  ql=[LI() for _ in range(q)]

  dic={}
  for i in range(h):
    for j in range(w):
      x=l[i][j]
      dic[x]=(i+1,j+1)

  n=h*w
  to_last_distance=[0]*n
  for i in range(1,n+1)[::-1]:
    if i+d<=n:
      i_y,i_x=dic[i]
      ipd_y,ipd_x=dic[i+d]
      to_last_distance[i-1]=to_last_distance[i+d-1]
      to_last_distance[i-1]+=(abs(i_y-ipd_y)+abs(i_x-ipd_x))

  # print(to_last_distance)

  ans=[]
  for st,ed in ql:
    ans.append(to_last_distance[st-1]-to_last_distance[ed-1])

  for x in ans:
    print(x)

main()
# print(main())

