import bisect

X, N = list(map(int, input().split()))
P = set(map(int, input().split()))

A = {i for i in range(102)}

S = list(A - P)

T = bisect.bisect_left(S, X)

if T == 0:
    print((S[0]))
elif X - S[T-1] > S[T] - X:
    print((S[T]))
else:
    print((S[T-1]))

