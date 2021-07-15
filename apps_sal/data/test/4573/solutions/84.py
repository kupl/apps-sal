import statistics
n = int(input())
X = list(map(int, input().split()))
X_ = sorted(X)
med = X_[n//2-1]
med_2 = X_[n//2]
for i in range(n):
    if X[i]>med:
        print(med)
    else:
        print(med_2)
