n = int(input())
l = list(map(int,input().split()))
l.sort()
d = set()
l[0] = 1
for i in range(1,n):
    l[i] = min(l[i-1] + 1,l[i])
print(l[n-1]+1)
