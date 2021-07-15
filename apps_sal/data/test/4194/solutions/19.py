n,m = list(map(int,input().split()))
a = list(map(int,input().split()))

ans = n
for i in range(m):
    ans -= a[i]

if ans < 0:
    print((-1))
else:
    print(ans)

