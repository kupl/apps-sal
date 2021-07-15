A,B,K = map(int,input().split())

X = min(A,B)
Y = []

for i in range(1,X+1):
    if (A % i == 0) and (B % i == 0):
        Y.append(i)

print(Y[-K])
