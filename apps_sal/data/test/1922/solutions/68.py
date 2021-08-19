(N, M) = list(map(int, input().split()))
if N >= 2 and M >= 2:
    print((N - 2) * (M - 2))
elif N == 1 and M >= 2:
    print(M - 2)
elif N >= 2 and M == 1:
    print(N - 2)
else:
    print('1')
