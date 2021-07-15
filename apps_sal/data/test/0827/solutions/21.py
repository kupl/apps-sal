N = int(input())
S = '110'*N
T = input()
ans = 0
for i in range(3):
  if S[i:i+N]==T:
    ans = pow(10,10)-(i+N-1)//3-i//3
    break
if T=='1':
  ans = 2*pow(10,10)
print(ans)
