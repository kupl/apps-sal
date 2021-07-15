import bisect
N, H = list(map(int, input().split()))
B = [0] * N
m = 0
for i in range(N):
  a, b = list(map(int, input().split()))
  B[i] = b
  m = max(m, a)
  
B = sorted(B)
index = bisect.bisect_left(B, m)
#print(index)

over = sum(B[index:])
if over >= H:
  #Bのみ
  now = 0
  i = 1
  while now < H:
    now += B[-i]
    i += 1
  print((i - 1))  
else:
  H -= over
  ans = N - index
  ans += int(H / m)
  if H % m != 0:
    ans += 1
  print(ans)
  
  

