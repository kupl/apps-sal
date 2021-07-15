N,L = map(int,input().split())
aji1 = []
ajimin = 1000

for i in range(1,N+1):
    aji1.append(L + i - 1)
    if abs(ajimin) >= abs(aji1[i-1]):
        ajimin = aji1[i-1]


print(sum(aji1)-ajimin)
