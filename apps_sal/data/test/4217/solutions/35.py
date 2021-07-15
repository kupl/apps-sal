n, m = map(int, input().split())
c = [0]*m

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(1, a[0]+1):
        c[a[j]-1] += 1
print(c.count(n))
