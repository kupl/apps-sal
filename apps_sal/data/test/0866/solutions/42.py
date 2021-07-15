X,Y = map(int,input().split())
M = 10**9+7
if X%3 == Y%3 == 1 or X%3 == Y%3 == 2:
    Answer = 0
else:
    dif = abs(X-Y)
    W =  (min(X,Y) - dif)//3
    X1 = W + dif
    Y1 = W
    Answer = 1
    N = X1+Y1
    for i in range(1,X1+1):
        Answer = (Answer*(N)*pow(i,-1,M))%M
        N -= 1
    for j in range(1,Y1+1):
        Answer = (Answer*(N)*pow(j,-1,M))%M
        N -= 1
print(Answer)
