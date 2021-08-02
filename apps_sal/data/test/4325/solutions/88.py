N, X, T = list(map(int, input().split()))
a = N / X
if a == int(a):
    print((int(a) * T))
else:
    print((int(a + 1) * T))
