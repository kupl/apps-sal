n = int(input())
v = list(map(int, input().split()))
cnt1 = [0 for i in range(100001)]
cnt2 = [0 for i in range(100001)]
for i in range(n):
    if i % 2 == 0:
        cnt1[v[i]] += 1
    else:
        cnt2[v[i]] += 1
k1 = 0
k1m = 0
k2 = 0
k2m = 0
for i in range(100001):
    if cnt1[i] >= cnt1[k1]:
        (k1, k1m) = (i, k1)
    elif cnt1[i] > cnt1[k1m]:
        k1m = i
for i in range(100001):
    if cnt2[i] >= cnt2[k2]:
        (k2, k2m) = (i, k2)
    elif cnt2[i] > cnt2[k2m]:
        k2m = i
if k1 != k2:
    print(n - cnt1[k1] - cnt2[k2])
else:
    print(n - (cnt1[k1] + max(cnt1[k1m], cnt2[k2m])))
