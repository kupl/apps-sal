n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = max(n - sum(a), -1)
print(ans)
