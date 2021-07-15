A, B, C, K = (int(x) for x in input().split())
AB = A + B
if K < A:
    print(K)
elif AB < K:
    print((A - (K-AB)))
else:
    print(A)

