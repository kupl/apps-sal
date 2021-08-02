a = list(map(int, input().split()))
N = a[0]
D = a[1]

z = N // (2 * D + 1)
if N % (2 * D + 1) == 0:
    print(z)
else:
    print(z + 1)
