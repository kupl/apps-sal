n = int(input())
a = list(map(int,input().split()))
a.sort()
j = a[-1]
for i in range(n):
    if a[i]*2 > j:
        break
if j - a[i-1]*2 > a[i]*2 - j:
    print(j,a[i])
else:
    print(j,a[i-1])
