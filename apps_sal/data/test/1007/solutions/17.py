import math
A = input().split()
k = int(A[0])
p = int(A[1])
palin = [0]*k
for i in range (0,k):
    digit = int(math.log(i+1) // math.log(10))
    L = list(str(i+1))
    M = L[::-1]
    fin = L+M
    num = ''.join(fin)
    palin[i] = int(num)
sum = 0
for i in range (0,k):
    sum = (sum + palin[i])%p
print(sum)
