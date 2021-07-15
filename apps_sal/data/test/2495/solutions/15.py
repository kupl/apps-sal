n = int(input())
a = list(map(int,input().split()))
ans = [0,0]

s = max(a[0],1)
ans[0] = abs(s-a[0])
for i in range(n-1):
    if s * (s + a[i+1]) >= 0:
        if s > 0:
            ans[0] += s + a[i+1] + 1
            s = -1
        else:
            ans[0] += 1 - (s + a[i+1])
            s = 1
    else:
            s += a[i+1]
s = min(-1,a[0])
ans[1] = abs(s-a[0])
for i in range(n-1):
    if s * (s + a[i+1]) >= 0:
        if s > 0:
            ans[1] += s + a[i+1] + 1
            s = -1
        else:
            ans[1] += 1 - (s + a[i+1])
            s = 1
    else:
            s += a[i+1]
print(min(ans))
