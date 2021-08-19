S = input()
T = input()
L = len(S) - len(T)
b = 0
if L > 0:
    a = [0] * L
    for i in range(L):
        for j in range(len(T)):
            if S[j + i] == T[j]:
                a[i] = a[i] + 1
    A = sorted(a, reverse=True)
    print(len(T) - A[0])
if L == 0:
    for l in range(len(S)):
        if S[l] == T[l]:
            b = b + 1
    print(len(T) - b)
