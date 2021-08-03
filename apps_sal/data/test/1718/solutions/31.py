N, K = list(map(int, input().split()))
A = list(int(x) for x in input().split())
if N <= 3:
    print((1))
    return
print((-(-(N - 1) // (K - 1))))
