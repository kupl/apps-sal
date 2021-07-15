N = int(input())
B = list(map(int, input().split()))
 
# A_1 <= B_1
# A_2 <= min(B_1, B_2)
# A_3 <= min(B_2, B_3)
# A_(N-1) <= min(B_(N-2), B_(N-1))
# A_N <= B_(N-1)
# ans = B_1 + min(B_1, B_2) + ... + min(B__(N-2), B_(N-1)) + B_(N-1)
 
ans = B[0] + B[N-2]
for i in range(1, N-1):
  ans += min(B[i-1], B[i])

print(ans)
