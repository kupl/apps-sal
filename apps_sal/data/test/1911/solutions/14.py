n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
t = []
for i in range(1,n):
    t.append(a[i]-a[i-1])
t.sort()
print(sum(t[:n-k]))

