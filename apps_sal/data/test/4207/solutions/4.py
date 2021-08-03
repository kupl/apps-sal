from collections import Counter
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


D = []
ANS = 0
for i in range(n):
    if A[i] == 0 and B[i] == 0:
        ANS += 1
    elif A[i] == 0 and B[i] != 0:
        continue
    elif A[i] != 0 and B[i] == 0:
        D.append(0)
    else:
        D.append((A[i] // gcd(A[i], B[i]), B[i] // gcd(A[i], B[i])))

C = Counter(D)

if len(C) == 0:
    print(ANS)
else:
    print(ANS + max(C.values()))
