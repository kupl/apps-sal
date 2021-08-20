(D, N) = map(int, input().split())
'\nq = (N-1)//99\nprint((100*q + N - 99*q)* 100**D)\n'
if N == 100:
    print(100 ** D * (N + 1))
else:
    print(100 ** D * N)
