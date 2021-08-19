(a1, b1) = list(map(int, input().split()))
(a2, b2) = list(map(int, input().split()))
(F, S) = ([a1, b1], [a2, b2])
A = dict()
B = dict()
A[2] = A[3] = B[2] = B[3] = 0
i = 2
while i ** 2 <= a1:
    if a1 % i == 0:
        A[i] = 0
        while a1 % i == 0:
            A[i] += 1
            a1 //= i
    i += 1
if a1 > 1:
    if not a1 in A:
        A[a1] = 0
    A[a1] += 1
i = 2
while i ** 2 <= b1:
    if b1 % i == 0:
        if not i in A:
            A[i] = 0
        while b1 % i == 0:
            A[i] += 1
            b1 //= i
    i += 1
if b1 > 1:
    if not b1 in A:
        A[b1] = 0
    A[b1] += 1
i = 2
while i ** 2 <= a2:
    if a2 % i == 0:
        B[i] = 0
        while a2 % i == 0:
            B[i] += 1
            a2 //= i
    i += 1
if a2 > 1:
    if not a2 in B:
        B[a2] = 0
    B[a2] += 1
i = 2
while i ** 2 <= b2:
    if b2 % i == 0:
        if not i in B:
            B[i] = 0
        while b2 % i == 0:
            B[i] += 1
            b2 //= i
    i += 1
if b2 > 1:
    if not b2 in B:
        B[b2] = 0
    B[b2] += 1
C1 = sorted([i for i in list(A.keys()) if not i in {2, 3}])
C2 = sorted([i for i in list(B.keys()) if not i in {2, 3}])
if C1 != C2:
    print(-1)
else:
    flag = True
    for i in C1:
        if A[i] != B[i]:
            flag = False
    if not flag:
        print(-1)
    else:
        Min = 0
        x = A[3] - B[3]
        Min += abs(x)
        if x >= 0:
            A[2] += x
            while x > 0 and F[0] % 3 == 0:
                F[0] //= 3
                F[0] *= 2
                x -= 1
            while x > 0 and F[1] % 3 == 0:
                F[1] //= 3
                F[1] *= 2
                x -= 1
        else:
            B[2] -= x
            while x < 0 and S[0] % 3 == 0:
                S[0] //= 3
                S[0] *= 2
                x += 1
            while x < 0 and S[1] % 3 == 0:
                S[1] //= 3
                S[1] *= 2
                x += 1
        if x != 0:
            flag = False
        x = A[2] - B[2]
        Min += abs(x)
        if x >= 0:
            while x > 0 and F[0] % 2 == 0:
                F[0] //= 2
                x -= 1
            while x > 0 and F[1] % 2 == 0:
                F[1] //= 2
                x -= 1
        else:
            while x < 0 and S[0] % 2 == 0:
                S[0] //= 2
                x += 1
            while x < 0 and S[1] % 2 == 0:
                S[1] //= 2
                x += 1
        if x != 0:
            flag = False
        if flag:
            print(Min)
            print(*F)
            print(*S)
        else:
            print(-1)
