(N, D) = map(int, input().split())
moniter = D * 2 + 1
if N <= moniter:
    print(1)
elif N % moniter == 0:
    print(N // moniter)
else:
    print(N // moniter + 1)
