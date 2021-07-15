N = int(input())
A_top = list(map(int,input().split()))
A_down = list(map(int,input().split()))
cnt_max = 0

for i in range(N):
  count = sum(A_top[:i+1]) + sum(A_down[i:])
  if count > cnt_max:
    cnt_max = count
    
print(cnt_max)

