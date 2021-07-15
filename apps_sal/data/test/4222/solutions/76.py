n, k = map(int, input().split())
d = [0]*k
a = [0]*k

for i in range(k):
    d[i] = int(input()) 
    a[i] = list(map(int, input().split()))

ans = [0]*100

for i in range(k):
    for j in range(d[i]):
        ans[a[i][j]-1] = 1

print(n-sum(ans))
