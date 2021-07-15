n = int(input())
p = list(map(int,input().split()))
c = list(map(int,input().split()))
k = 1
for i in range(n-1):
    if c[i+1] != c[p[i]-1]:
        k+= 1
print(k)
