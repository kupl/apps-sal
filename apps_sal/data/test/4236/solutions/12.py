n, m = map(int, input().split())
a = [0]*(m+1)
for i in range(n):
    l, r = map(int, input().split())
    while l!=r+1:
        a[l] = 1
        l+=1

print(a.count(0)-1)
for i in range(1,m+1):
    if a[i]==0:
        print(i, end = ' ')
