a=[int(i) for i in input().split()]

a.sort(reverse=True)

ans=a[0]*10+a[1]+a[2]
print(ans)
