import sys
readline = sys.stdin.readline

N = int(readline())
A = list(map(int,readline().split()))

def isOk(xor, val):
  while xor and val:
    if xor & 1 and val & 1:
      return False
    xor >>= 1
    val >>= 1
  return True
  
xor = 0
right = 0
ans = 0
for left in range(N):
  while right < N and isOk(xor, A[right]):
    xor ^= A[right]
    right += 1
  ans += right - left
  
  if left == right:
    right += 1
  else:
    xor ^= A[left]
    
print(ans)
