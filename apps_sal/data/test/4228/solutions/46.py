N, L = map(int, input().split())
S = (2*L+N-1)*N // 2
if L <= 0 <= L+N-1:
  ans = S
elif L < 0:
  ans = S - (L+N-1)
else:
  ans = S - L
print(ans)
