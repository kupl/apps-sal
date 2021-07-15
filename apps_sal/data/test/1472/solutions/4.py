def main():
  N, X, Y = map(int, input().split())
  G = [[i] for i in range(1,N+1)]
  ans=[0]*(N-1)
  for i in range(1,N+1):
    for j in range(i+1,N+1):
      d = min(j-i, abs(X-i)+1+abs(j-Y), abs(Y-i)+1+abs(j-X))
      #print(i,j,d)
      ans[d-1]+=1
  for a in ans:
    print(a)

def __starting_point():
  main()
__starting_point()
