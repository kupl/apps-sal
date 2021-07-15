N = int(input())
A = list(map(int,input().split()))
ans_list = [0]*N

for i in range(N-1):
  ans_list[A[i]-1] += 1
  
for j in range(N):
  print(ans_list[j])
