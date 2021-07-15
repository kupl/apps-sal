n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    a[i] = (a[i], i + 1)
a.sort()
for i in range(n//2):
    print(a[i][1], a[n-i-1][1])
