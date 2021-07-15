N = int(input())
A = list(map(int,input().split()))

A.sort()
retval = 0
for i in range(1,N):
  retval+=A[N-i//2-1]
  #print(N-i//2-1)
print(retval)
