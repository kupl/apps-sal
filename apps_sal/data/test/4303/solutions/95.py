n,k = map(int, input().split())
lis = list(map(int, input().split()))

if len(lis) == 1:
    print(abs(lis[0]))
    return

ans = 10**9+7
for i in range(n-k+1):
    l = abs(lis[i]) + abs(lis[i+k-1]-lis[i])
    r = abs(lis[i+k-1]) + abs(lis[i+k-1]-lis[i])
    ans = min(ans, l, r)

print(ans)
