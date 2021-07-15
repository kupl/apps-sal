N = int(input())

ans = ''
while(N > 0):
  N -= 1
  _i = N % 26
  ans = chr(ord('a') + _i) + ans
  N //= 26
  
print(ans)
