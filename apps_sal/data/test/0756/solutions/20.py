n=int(input())
a=[int(i) for i in input().split(' ')]
a.insert(0,0)
for i in range(1,n+1):
    if a[i]-a[i-1]>15:
        print(a[i-1]+15)
        break
else:
    print(min(a[n]+15,90))
