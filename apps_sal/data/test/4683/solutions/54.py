N, = map(int,input().split())
A = list(map(int,input().split()))
su = A[N-1]
suu = su*A[N-2]
for i in reversed(range(1,N-1)):
  su+=A[i]
  suu+=(su*A[i-1])
print(suu%(10 ** 9+7))
