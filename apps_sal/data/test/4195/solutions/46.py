D, N = list(map(int, input().split()))
if D > 0:
  if N < 100:
    print(( N * 100**D ))
  else:
    print(( 101 * 100**D ))
if D == 0:
  if N < 100:
    print(N)
  else:
    print((101))

