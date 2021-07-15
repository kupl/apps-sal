import copy
N = int(input())
A = [int(x) for x in input().split()]
suma = sum(A)
x0 = 0
for i in range(N) :
    x0 += ((-1)**i) * A[i]

x = [x0]

for i in range(1,N) :
    xi = (A[i-1] - x[i-1]//2)*2
    x.append(xi)

for i in range(N) :
    print(x[i],end=' ')
