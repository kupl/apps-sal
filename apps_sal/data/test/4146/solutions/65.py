from collections import Counter
n=int(input())
a=list(map(int,input().split()))

f=Counter(a[0::2]).most_common(2)
b=Counter(a[1::2]).most_common(2)

if f[0][0]!=b[0][0]:print(n-f[0][1]-b[0][1]);return

if f[0][1]==n//2:print(n//2)
else:print(n-b[0][1]-f[1][1] if f[1][1]>b[1][1] else n-f[0][1]-b[1][1])
