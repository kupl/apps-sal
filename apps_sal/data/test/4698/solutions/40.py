N = int(input())
T = list(map(int,input().split()))

t_sum = sum(T)

M = int(input())
for _ in range(M):
  P,X = map(int,input().split())
  print(t_sum - (T[P-1] - X))
