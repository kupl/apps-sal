D, N = map(int, input().split())
if N != 100:
  if D == 0:
    print(N)
  elif D == 1:
    x = [100 * i for i in range(1, 101)]
    print(x[N-1])
  elif D == 2:
    x = [10000 * i for i in range(1, 101)]
    print(x[N-1])
else:
  if D == 0:
    print(101)
  elif D == 1:
    x = [100 * i for i in range(1, 101)]
    print(x[N-1]+100)
  elif D == 2:
    x = [10000 * i for i in range(1, 101)]
    print(x[N-1]+10000)
