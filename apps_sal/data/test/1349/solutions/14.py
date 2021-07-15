
def solve(n,X):

  a = X[0]-1
  b = n-X[-1]
  c = max((X[i+1]-X[i] for i in range(len(X)-1)),default=0)//2

  return max(a,b,c)+1





T = int(input())
for _ in range(T):
  n,k = map(int,input().split())
  X = tuple(map(int,input().split()))
  print(solve(n,X))
