import math as m
n, k = map(int, input().split())
A = list(map(int, input().split()))
kl = 0
dl = 0
t = 0
Pr = [0] * k
Nm = [-1] * k
Rz = [False] * n

while dl < n:

    for i in range(k):
        Pr[i] -= 1
        if Pr[i] == -1:
            if Nm[i] != -1:
                dl += 1
            if kl < n:
                Pr[i] = A[kl] - 1
                Nm[i] = kl
                kl += 1
            else:
                Nm[i] = -1
                Pr[i] = -1
    for i in range(k):
        if m.floor(dl / n * 100 + 0.5) == A[Nm[i]] - Pr[i] and Nm[i] != -1:
            Rz[Nm[i]] = True
    t += 1
print(sum(Rz))
