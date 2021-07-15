n, k = map(int, input().split())

ans = min(n%k, abs(n%k - k))
print(ans)
