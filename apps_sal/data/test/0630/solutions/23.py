n, k = (int(s) for s in input().split())
a = [0] + [int(s) for s in input().split()]
ans = [0,]

for i in range(1, n + 1):
    if not a[i]:
        ans.append( min(i - 1, k) + 1 + min(n - i, k) )
    else:
        if a[i] + k < i - k:
            ans.append( min(i - 1, k) + 1 + min(n - i, k) + ans[a[i]] )
        else:
            ans.append( ans[a[i]] + min(n, i + k) - a[i] - min(k, n - a[i]))
    
print(*ans[1:])
