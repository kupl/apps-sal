n, m, k = list(map(int, input().split()))
v = list(map(int, input().split()))

available = 0
v.sort(reverse = True)
ans = -1

if k >= m:
    ans = 0
else:
    for i in range(n):
        if i < k:
            available += v[i]
        else:
            available += v[i]-1
        if(available + max(0, k-i-1) >= m):
            ans = i+1
            break

print (ans)





