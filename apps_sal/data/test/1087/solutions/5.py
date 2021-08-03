n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
bounded = True
for i in range(40, -1, -1):
    d = 1 << i
    cnt1 = sum(d & ai > 0 for ai in a)
    cnt0 = n - cnt1
    if bounded and k & d == 0 or cnt1 >= cnt0:
        ans += cnt1 * d
        if k & d > 0:
            bounded = False
    else:
        ans += cnt0 * d
print(ans)
