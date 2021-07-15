k, n = list(map(int, input().split()))
a = list(map(int, input().split()))
dis = min(abs(a[0] - a[-1]), abs(k + a[0] - a[-1]))
for i in range(n-1):
    dis = max(dis, abs(a[i+1] - a[i]))
ans = k - dis
print(ans)

