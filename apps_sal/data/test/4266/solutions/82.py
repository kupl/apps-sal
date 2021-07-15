K,X = map(int,input().split())
P = []
for i in range(-K+1,K):
    P.append(X+i)
print(" ".join(map(str,P)))
