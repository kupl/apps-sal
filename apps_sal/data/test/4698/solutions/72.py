N = int(input())
T = list(map(int, input().split()))
sumT = sum(T)
M = int(input())
for i in range(M):
  P, X = map(int, input().split())
  ans = sumT-T[P-1]+X
  print(ans)
