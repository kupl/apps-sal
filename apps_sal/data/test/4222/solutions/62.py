N,K = map(int,input().split())
ls = [0]*(N+1)
for i in range(K):
    d = int(input())
    ls1 = list(map(int,input().split()))
    for j in ls1:
        ls[j] += 1
ans = ls.count(0)-1
print(ans)
