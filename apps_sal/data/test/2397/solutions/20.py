n, k = list(map(int, input().strip().split(' ')))
a = list(map(int, input().strip().split(' ')))
cnt = []
cnt.append(a[-1])
for i in range(1, n):
 cnt.append(cnt[i-1] + a[-(i+1)])
ans = cnt[-1]
del cnt[-1]
cnt.sort(reverse=True)
ans += sum(cnt[:(k-1)])
print(ans)

