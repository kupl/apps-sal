import math
from fractions import gcd


def primes(limit):
    Ans = []
    C = [True] * (limit + 1)
    L = list(range(2, limit + 1))
    for item in L:
        if C[item]:
            i = 2
            while item * i <= limit:
                C[item * i] = False
                i += 1
    for item in L:
        if C[item]:
            Ans += [item]
    return Ans


(a, b) = list(map(int, input().split()))
aa = a
bb = b
A = []
B = []
p = primes(int(math.sqrt(10 ** 9)))
for i in range(len(p)):
    if p[i] > a:
        break
    while a % p[i] == 0:
        A.append(p[i])
        a //= p[i]
if a != 1:
    A.append(a)
for i in range(len(p)):
    if p[i] > b:
        break
    while b % p[i] == 0:
        B.append(p[i])
        b //= p[i]
if b != 1:
    B.append(b)
if aa == 1 and bb == 1:
    print(0)
elif aa == 1:
    Done = True
    for item in B:
        if item > 5:
            Done = False
            break
    if Done:
        print(len(B))
    else:
        print(-1)
elif bb == 1:
    Done = True
    for item in A:
        if item > 5:
            Done = False
            break
    if Done:
        print(len(A))
    else:
        print(-1)
else:
    B.sort()
    A.sort()
    Done = True
    ind = 0
    ans = 0
    while A != B:
        if ind >= len(A) and ind >= len(B):
            Done = False
            break
        elif ind >= len(A):
            if B[-1] > 5:
                Done = False
                break
            else:
                ans += len(B) - ind
                break
        elif ind >= len(B):
            if A[-1] > 5:
                Done = False
                break
            else:
                ans += len(A) - ind
                break
        if A[ind] == B[ind]:
            ind += 1
            continue
        if A[ind] < B[ind]:
            if A[ind] > 5:
                Done = False
                break
            else:
                ans += 1
                A.pop(ind)
        elif B[ind] > 5:
            Done = False
            break
        else:
            ans += 1
            B.pop(ind)
    if Done:
        print(ans)
    else:
        print(-1)
