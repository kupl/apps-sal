N = int(input())
X = list(map(int,input().split()))
Y = sorted(X)
med = (Y[N//2] + Y[N//2-1])/2
for i in range(N):
    if X[i] <= med:
        print(Y[N//2])
    else:
        print(Y[N//2-1])
