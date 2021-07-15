N = int(input())
B = list(map(int, input().split()))

# A_1 <= B_1
# A_2 <= min(B_1, B_2)
# A_3 <= min(B_2, B_3)
# A_(N-1) <= min(B_(N-2), B_(N-1))
# A_N <= B_(N-1)
# ans = B_1 + min(B_1, B_2) + ... + min(B__(N-2), B_(N-1)) + B_(N-1)
 
ans = 0
for i in range(N):
  if i == 0: ans += B[0]
  elif i == N-1: ans += B[N-2]
  else: ans += min(B[i-1], B[i])

print(ans)
