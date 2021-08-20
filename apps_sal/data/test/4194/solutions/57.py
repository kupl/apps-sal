(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
ans = -1
if sum(l) <= n:
    ans = n - sum(l)
print(ans)
