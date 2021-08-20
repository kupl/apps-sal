(N, A, B) = list(map(int, input().split()))
if A == 0 and B == 0:
    print(0)
elif A == 0:
    print(0)
elif B == 0:
    print(N)
else:
    (q, mod) = divmod(N, A + B)
    print(min(mod, A) + q * A)
