N,K = list(map(int,input().split()))
L = sorted(list(map(int,input().split())))
B = [True for n in range(N)]
P = 0
i = 0
j = N//2
while i < N and j < N:
    while j < N and L[i]+K > L[j]: j += 1
    if i < j < N and B[i] and B[j]:
        B[i] = False
        B[j] = False
        P += 1
    i += 1
    j += 1
print(P)

