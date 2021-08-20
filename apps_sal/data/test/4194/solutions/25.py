(n, _) = map(int, input().split())
ans = n - sum(map(int, input().split()))
if ans < 0:
    ans = -1
print(ans)
