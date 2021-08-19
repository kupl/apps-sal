(n, k) = list(map(int, input().split()))
h = list(map(int, input().split()))
ans = len([i for i in h if i >= k])
print(ans)
