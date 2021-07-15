A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0
for i in range(A+1):
    X_ = X
    X_ -= 500*i
    for j in range(B+1):
        X__ = X_
        X__ -= 100*j
        for k in range(C+1):
            X___ = X__
            X___ -= 50*k
            if X___ == 0:
                cnt += 1
print(cnt)
