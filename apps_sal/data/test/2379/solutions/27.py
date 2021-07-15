def main():
  N, K, C=list(map(int, input().split()))
  S = input()[::-1]
  
  R=[0]*K
  n, k=0, 0
  while k < K:
    if S[n]=='o':
      R[k]=N-n
      k+=1
      n += C
    n+=1
  R=R[::-1]
  
  S=S[::-1]
  n, k=0, 0
  while k < K:
    if S[n]=='o':
      if n+1 == R[k]:
        print((n+1))
      k+=1
      n += C
    n+=1
  #print(L)
  
def __starting_point():
  main()

__starting_point()
