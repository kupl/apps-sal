n = int(input())
a = list(map(int,input().split()))
ans = 0
if a == sorted(a):
    print(ans)
    return
b = a.index(max(a))
for i in range(0,b):
    if a[i] > a[i+1]:
        ans = ans + a[i]-a[i+1]
        a[i+1] = a[i]
ans = ans + max(a)*len(a[b+1:])-sum(a[b+1:])
print(ans)
