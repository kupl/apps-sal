(D, N) = list(map(int, input().split()))
if D == 0 and N != 100:
    print(N)
if D == 0 and N == 100:
    print(101)
if D == 1 and N != 100:
    print(N * 100)
if D == 1 and N == 100:
    print(10100)
if D == 2 and N != 100:
    print(N * 10000)
if D == 2 and N == 100:
    print(1010000)
