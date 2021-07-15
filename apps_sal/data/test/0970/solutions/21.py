n = int(input())
P = input().split(' ')
for i in range(n//2):
    P[i] = int(P[i])
P.sort()
B = [0] * (n//2)
W = [0] * (n//2)
for i in range(n//2):
    B[i] = 2*i+1
    W[i] = 2*i+2
b = 0
w = 0
for i in range(n//2):
    b+=abs(B[i]-P[i])
    w+=abs(W[i]-P[i])
print(min(b, w))

