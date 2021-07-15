N = int(input())
T = list(map(int,input().split()))
M = int(input())

for m in range(M):
  P,X = list(map(int,input().split()))
  T_ans = T.copy()
  T_ans[P-1] = X
  print((sum(T_ans)))

