n = int(input())
A = list(map(int, input().split()))

A0 = [a for a in A if a % 2 == 0]
A1 = [a for a in A if a % 2 == 1]

A0.sort()
A1.sort()

L0 = len(A0)
L1 = len(A1)

if abs(L0 - L1) <= 1:
    print(0)

elif L0 > L1:
    x = L0 - L1 - 1
    print(sum(A0[:x]))

elif L0 < L1:
    x = L1 - L0 - 1
    print(sum(A1[:x]))
