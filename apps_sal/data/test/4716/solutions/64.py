n,k = map(int,input().split())
li = list(map(int,input().split()))
li.sort(reverse=True)
tol = 0
for i in range(k):
    tol += li[i]
print(tol)
