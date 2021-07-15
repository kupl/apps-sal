N = int(input())
T = list(map(int, input().split()))
M = int(input())
for i in range(M):
  p, x = list(map(int, input().split()))
  s = sum(T) - T[p-1] + x
  print(s)
  

