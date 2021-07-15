n=int(input())
ar=list(map(int,input().split()))
ar.sort()
fl=False
for i in range(1,n-1):
    if ar[n-i]<ar[n-i-1]+ar[n-i-2]:
        fl=True
        break
if fl:
    print("YES")
else:
    print("NO")

