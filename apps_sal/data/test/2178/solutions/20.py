n = int(input())

a = [int(s) for s in input().split()]
x = [int(s) for s in input().split()]

c = [0]*(n+1)
for i in range(n):
    c[a[i]] = i+1

mx = 0

for i in x:
    if c[i]>mx:
        print(c[i] - mx, end=' ')
        mx = c[i]
    else:
        print(0, end=' ')
