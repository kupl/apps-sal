N = int(input())
M = int(input())
if N > 32:
    print(M)
else:
    print(M % (1 << N))
