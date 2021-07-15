n = int(input())
a = list(map(int,input().split()))
a.sort()

if (a[n-1] < a[n-2] + a[n-3]) :
    print("YES")
    a[n-1],a[n-2] = a[n-2],a[n-1]
    print(" ".join(map(str,a)))
else:
    print("NO")

