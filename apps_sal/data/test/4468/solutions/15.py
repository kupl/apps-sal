n, t = map(int, input().split())
l = list(map(int, input().split()))
old = 0
ans = t
for i in range(1,n):
    ans += l[i] + t - max(old + t,l[i])
    old = l[i]
print(ans)
