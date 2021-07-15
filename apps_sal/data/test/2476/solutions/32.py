n = int(input())
A = list(map(int,input().split()))
B = [0]*(n+1)
C = [0]*(n+1)
for a in A:
    B[a] += 1
    C[B[a]] += 1

X = [0]
for i in range(1,n+1):
    X.append(X[i-1] + C[i])
for j in range(1,n+1):
    X[j] = X[j] // j

ind = n
k = 1
while k<=n:
    if ind<0:
        for _ in range(n-k+1):
            print(0)
        break
    if k<=X[ind]:
        print(ind)
        k += 1
    else:
        ind -= 1
