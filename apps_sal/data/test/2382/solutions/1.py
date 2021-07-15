N = int(input())
N2 = 2**N
S = list(map(int, input().split()))
S.sort(reverse=True)

slimes = [S[0]]
S[0] = float('inf')
num = 1
for i in range(N):
  slimes.sort()
  n = num
  idx = 0
  while n and idx<=N2-1:
    if S[idx] < slimes[n-1]:
      slimes.append(S[idx])
      S[idx] = float('inf')
      idx += 1
      n -= 1
    else:
      idx += 1
  
  if n:
    print('No')
    return
  
  num *= 2

print('Yes')
