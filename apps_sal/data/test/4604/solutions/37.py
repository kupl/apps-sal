from collections import Counter
N = int(input())
A = list(map(int, input().split()))
MOD = int(1000000000.0) + 7
if N % 2 == 0:
    c = Counter(A)
    if all((i == 2 for i in c.values())):
        print(pow(2, N // 2, MOD))
    else:
        print(0)
else:
    A.sort()
    A = A[1:]
    c = Counter(A)
    if all((i == 2 for i in c.values())):
        print(pow(2, N // 2, MOD))
    else:
        print(0)
