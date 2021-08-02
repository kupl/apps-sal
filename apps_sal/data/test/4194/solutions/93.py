n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = n - sum(arr)
print(max(-1, ans))
