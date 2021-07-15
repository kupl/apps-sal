N = int(input())
N2 = 2**N
S = list(map(int, input().split()))
S.sort(reverse=True)

slimes = [S[0]]
S[0] = float('inf')
num = 1
min_idx = 1
for i in range(N):
  slimes.sort()
  n = num
  idx = min_idx
  is_continuous = True
  while n and idx<=N2-1:
    if S[idx] < slimes[n-1]:
      slimes.append(S[idx])
      S[idx] = float('inf')
      idx += 1
      n -= 1
      min_idx += is_continuous
    else:
      if S[idx] < float('inf'):
        is_continuous = False
      idx += 1
      min_idx += is_continuous
  
  if n:
    print('No')
    return
  
  num *= 2

print('Yes')
