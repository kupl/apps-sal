n, m, x = map(int, input().split())
a = list(map(int, input().split()))
cnt1, cnt2 = 0, 0
for i in range(m):
    if 0 <= a[i] < x:
        cnt1 += 1
    if x < a[i] <= a[-1]:
        cnt2 += 1
print(min(cnt1, cnt2))
