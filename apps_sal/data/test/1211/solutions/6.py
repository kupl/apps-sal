n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
m = [0]*k
for i in range(k):
    m[i] = n%a[i]
i = m.index(min(m))+1
print(i, n//a[i-1])


