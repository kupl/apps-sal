n = int(input())
a = list(map(int, input().split()))
pre = a[:]
cnt1 = [1] * n
for i in range(len(a)):
    if i == 0:
        continue
    pre[i] = pre[i - 1]
    cnt1[i] = cnt1[i - 1]
    if a[i] < pre[i]:
        pre[i] = a[i]
        cnt1[i] = 1
    elif a[i] == pre[i]:
        cnt1[i] += 1
pre2 = [10 ** 30] * n
cnt2 = [0] * n
for i in range(n):
    if i == 0:
        continue
    pre2[i] = pre2[i - 1]
    cnt2[i] = cnt2[i - 1]
    te = a[i] * pre[i - 1]
    if te < pre2[i]:
        pre2[i] = te
        cnt2[i] = cnt1[i - 1]
    elif te == pre2[i]:
        cnt2[i] += cnt1[i - 1]
ans = 10 ** 30
cnt = 0
for i in range(n):
    if i < 2:
        continue
    t = a[i] * pre2[i - 1]
    if t < ans:
        ans = t
        cnt = cnt2[i - 1]
    elif ans == t:
        cnt += cnt2[i - 1]
print(cnt)
