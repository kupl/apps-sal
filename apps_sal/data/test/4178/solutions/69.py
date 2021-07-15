N = int(input())
H = list(map(int,input().split()))

for i in range(N-1):
  if H[i+1] == H[i]-1:
    H[i+1] = H[i]
  elif H[i+1] >= H[i]:
    continue
  else:
    print('No')
    return
print('Yes')
