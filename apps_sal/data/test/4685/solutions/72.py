List =  list(map(int, input().split()))
K = int(input())
sort = sorted(List)
for i in range(K):
    sort[-1] = sort[-1]*2
print((sum(sort)))    

