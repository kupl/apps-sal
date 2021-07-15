n = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
if n % 2:
    print(a[0]+a[n//2]+2*(sum(a[1:(n-1)//2])))
else:
    print(a[0]+2*(sum(a[1:n//2])))
