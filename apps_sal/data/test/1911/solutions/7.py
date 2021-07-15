n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = a[-1] - a[0]
delta = [-a[i] + a[i - 1] for i in range(1, n)]
delta.sort()
ans += sum(delta[:(k-1)])
print(ans)
