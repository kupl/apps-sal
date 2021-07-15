a =  int(input())
Ans = []
for i in range(a):
    B = []
    x = int(input())
    A = list(map(int, input().split()))
    C = []
    for j in range(1, len(A) + 1):
        C.append([j, 0])
    k = 1
    n = 0
    for j in range(len(A)):
        if A[j] >k:
            B.append(A[j])
            k = A[j]
            C[A[j] - 1][1] = 1
        else:
            while C[n][1] == 1:
                n += 1
            C[n][1] = 1
            B.append(n + 1)
    b0 = B[0]
    Tr = True
    for j in range(len(B)):
        b0 = max(b0, B[j])
        if A[j] != b0:
            Tr = False
    if Tr:
        Ans.append(B)
    else:
        Ans.append([-1])
    #Ans.append(B[-1])
for b in Ans:
    print(*b)

