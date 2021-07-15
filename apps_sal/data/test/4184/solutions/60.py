import copy
n = int(input())
W = list(map(int, input().split()))

m = abs(sum(W)-W[0])
L = W[0]

for i in range(1, n-1):
    L += W[i]
    m = min(abs(sum(W)-2*L), m)
    
print(m)

