k, n = map(int, input().split())
a = list(map(int, input().split()))
root = []
ans = 0

for i in range(0, n-1):
    x = a[i+1] - a[i]
    root.append(x)

y = a[0] + k - a[n-1]
root.append(y)

for i in root:
    ans += i

ans -= max(root)
print(ans)    
