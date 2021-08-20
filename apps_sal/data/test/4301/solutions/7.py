import copy
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
amax = max(A)
amaxindex = A.index(amax)
B = copy.deepcopy(A)
del B[amaxindex]
bmax = max(B)
for i in range(N):
    if i == amaxindex:
        print(bmax)
    else:
        print(amax)
