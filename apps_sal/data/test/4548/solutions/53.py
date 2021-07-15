n, m, x = map(int, input().split())

a = list(map(int, input().split()))

r = 0
for i in range(x+1,n):
    for j in range(m):
        if i == a[j]:
            r += 1

l = 0
for i in range(x-1, -1, -1):
    for j in range(m):
        if i == a[j]:
            l += 1
        
print(min(l,r))
