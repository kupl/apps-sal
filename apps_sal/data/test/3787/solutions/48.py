N, A, B = map(int, input().split())

if A * B < N:
  print(-1)
elif A + B - 1 > N:
  print(-1)
else:
  P = [0] * N
  b = (N - A) // (B - 1) if B > 1 else 0
  r = (N - A) % (B - 1) + 1 if B > 1 else 1
  i = 1
  pos = 0
  while i <= N:
    if b:
      for j in range(B):
        P[pos + B - j - 1] = i
        i += 1
      pos += B
      b -= 1
    elif r:
      for j in range(r):
        P[pos + r - j - 1] = i
        i += 1
      pos += r
      r = 0
    else:
      P[pos] = i
      i += 1
      pos += 1
    
  for p in P:
    print(p, end=' ')
