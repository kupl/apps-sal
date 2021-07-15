import copy
N = int(input())
X = list(map(int, input().split()))
Xsort = copy.copy(X)
Xsort.sort()
centerR = Xsort[N//2]
centerL = Xsort[N//2-1]
for i in range(N):
    if X[i] >= centerR:
        print(centerL)
    else:
        print(centerR)

