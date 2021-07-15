A,B,K = list(map(int,input().split()))
if B - A >= 2 * K :
  for i in range(K):
    print((A + i))
  for j in reversed(list(range(K))):
    print((B - j))
else:
  for _ in range(A,B + 1):
    print(_)

