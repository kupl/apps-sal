N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

Bit = 0
while(True):
    if((1 << (Bit + 1)) > K):
        break
    else:
        Bit += 1
X = 0
for b in range(Bit, -1, -1):
    X_ = X + (1 << b)
    if(X_ > K):
        continue
    Sum = sum([X ^ a for a in A])
    Sum_ = sum([X_ ^ a for a in A])
    if(Sum_ > Sum):
        X = X_
print((sum([X ^ a for a in A])))
