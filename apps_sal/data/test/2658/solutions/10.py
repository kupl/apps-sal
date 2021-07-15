n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
rec = [0]
i = 0
flag = [0 for _ in range(n + 1)]
while True:
    if flag[rec[i]] == 0:
        flag[rec[i]] = 1
        rec.append(a[rec[i]] - 1)
    else:
        start = rec.index(a[rec[i]] - 1)
        loop = rec[start:]
        pre = rec[:start]
        break
    i += 1
count = (k - len(pre)) % len(loop)
if k <= len(pre):
    print((pre[k] + 1))
else:
    print((loop[count] + 1))

