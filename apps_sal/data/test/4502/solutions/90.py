N = int(input())
A = list(map(int,input().split()))

# 0
# 1, 0
# 2, 0, 1
# 3, 1, 0, 2
# 4, 2 ,0, 1, 3

front = []
back = []

for i in range(N):
  if i % 2 == 0:
    back.append(A[i])
  else:
    front.append(A[i])
    
ans = None
if N % 2 == 0:
  ans = front[::-1] + back
else:
  ans = back[::-1] + front
  
print(*ans)
