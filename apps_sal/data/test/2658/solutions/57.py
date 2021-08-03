n, k = map(int, input().split())
a = list(map(int, input().split()))
l = [0] * n
i = 0
cnt = 0
while l[i] == 0:
    l[i] = a[i]
    i = a[i] - 1
    cnt += 1
start = i + 1
i = 0
pre = 0
while i + 1 != start:
    i = a[i] - 1
    pre += 1
loop = cnt - pre
if pre + loop < k:
    k = (k - pre) % loop + pre
i = 0
for _ in range(k):
    i = a[i] - 1
print(i + 1)
