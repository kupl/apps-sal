r = input().split()
N = int(r[0])
D = int(r[1])
if N % (2 * D + 1) == 0:
    print(N // (2 * D + 1))
else:
    print(N // (2 * D + 1) + 1)
