(n, k) = map(int, input().split())
cnt1 = 0
cnt2 = 0
for i in range(1, n + 1):
    if i % k == 0:
        cnt1 += 1
    if i % k == k // 2:
        cnt2 += 1
ans = cnt1 ** 3 if k % 2 == 1 else cnt1 ** 3 + cnt2 ** 3
print(ans)
