(n, k, p, x, y) = list(map(int, input().split()))
b = list(map(int, input().split()))
lower_bound = 1
for i in range(k):
    if b[i] < y:
        lower_bound += 1
ans = [1] * min((n + 1) // 2 - lower_bound, n - k)
while len(ans) < n - k:
    ans.append(y)
if sum(ans + b) <= x and (n + 1) // 2 - lower_bound >= 0 and (p >= y):
    print(' '.join(map(str, ans)))
else:
    print('-1')
