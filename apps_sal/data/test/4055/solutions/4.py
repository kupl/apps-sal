n = int(input())
T = input().split(' ')
for i in range(n):
    T[i] = int(T[i])
m = 0
for i in range(1, n-1):
    if T[i-1]==1 and T[i]==0 and T[i+1] == 1:
        m+=1
        T[i+1] = 0
print(m)

