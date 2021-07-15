N,K = map(int,input().split())
n_lis = [0]*N
for i in range(K):
    d = int(input())
    *A, = map(int,input().split())
    for j in range(d):
        a = A[j]
        n_lis[a-1] = 1
print(n_lis.count(0))   
